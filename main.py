import json
import logging
import random
import time
import uuid

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)


def write_log(endpoint, status, response_time_ms, severity="INFO"):
    log_entry = {
        "request_id": str(uuid.uuid4()),
        "endpoint": endpoint,
        "method": request.method,
        "status": status,
        "response_time_ms": round(response_time_ms, 2),
        "severity": severity,
        "event_type": "REQUEST",
        "service": "cloud-log-analysis"
    }

    logging.info(json.dumps(log_entry))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    start = time.time()

    response = {
        "service": "cloud-log-analysis",
        "status": "healthy"
    }

    latency = (time.time() - start) * 1000
    write_log("/health", 200, latency)

    return jsonify(response), 200


@app.route("/api/data")
def api_data():
    start = time.time()

    # Simulates realistic application behaviour
    outcome = random.choices(
        ["success", "not_found", "error", "slow"],
        weights=[70, 10, 10, 10],
        k=1
    )[0]

    if outcome == "slow":
        time.sleep(random.uniform(1.2, 2.5))

    latency = (time.time() - start) * 1000

    if outcome == "error":
        write_log(
            "/api/data",
            500,
            latency,
            "ERROR"
        )

        return jsonify(
            error="Internal service failure"
        ), 500

    if outcome == "not_found":
        write_log(
            "/api/data",
            404,
            latency,
            "WARNING"
        )

        return jsonify(
            error="Resource not found"
        ), 404

    write_log(
        "/api/data",
        200,
        latency,
        "INFO"
    )

    return jsonify(
        message="Data retrieved successfully",
        latency_ms=round(latency, 2)
    ), 200


@app.route("/api/orders")
def orders():
    start = time.time()

    time.sleep(random.uniform(0.05, 0.5))

    latency = (time.time() - start) * 1000

    write_log(
        "/api/orders",
        200,
        latency
    )

    return jsonify(
        orders=random.randint(10, 100),
        latency_ms=round(latency, 2)
    ), 200


@app.route("/api/analytics")
def analytics():
    start = time.time()

    time.sleep(random.uniform(0.2, 1.0))

    latency = (time.time() - start) * 1000

    write_log(
        "/api/analytics",
        200,
        latency
    )

    return jsonify(
        status="processed",
        latency_ms=round(latency, 2)
    ), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
