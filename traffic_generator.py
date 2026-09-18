import random
import time
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python traffic_generator.py <SERVICE_URL>")
    sys.exit(1)

BASE_URL = sys.argv[1].rstrip("/")

endpoints = [
    "/api/data",
    "/api/orders",
    "/api/analytics",
    "/health"
]

weights = [50, 20, 20, 10]

TOTAL_REQUESTS = 150

print(f"Generating {TOTAL_REQUESTS} requests...")
print(f"Target: {BASE_URL}\n")

successful = 0
failed = 0

for i in range(1, TOTAL_REQUESTS + 1):

    endpoint = random.choices(
        endpoints,
        weights=weights,
        k=1
    )[0]

    start = time.time()

    try:
        response = requests.get(
            BASE_URL + endpoint,
            timeout=10
        )

        latency = (time.time() - start) * 1000

        if response.status_code < 400:
            successful += 1
        else:
            failed += 1

        print(
            f"[{i:03}/{TOTAL_REQUESTS}] "
            f"{endpoint:<15} "
            f"HTTP {response.status_code} "
            f"{latency:.0f} ms"
        )

    except requests.RequestException as error:
        failed += 1
        print(f"[{i:03}] REQUEST FAILED: {error}")

    time.sleep(random.uniform(0.05, 0.20))

print("\nTraffic generation complete.")
print(f"Successful: {successful}")
print(f"Failed:     {failed}")
