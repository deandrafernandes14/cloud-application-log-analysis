# Cloud Application Log Analysis System

A cloud-native application monitoring and log analytics system built on Google Cloud Platform. The system collects application logs, identifies errors, failed requests and abnormal activity, and generates an application health dashboard.

## Architecture

Cloud Run → Cloud Logging → Log Router → BigQuery → Looker Studio

## Features

- Serverless Flask application deployed on Google Cloud Run
- Automatic application and HTTP request logging
- Error and failed-request detection
- Abnormal activity and latency monitoring
- Automated traffic generator for load simulation
- Cloud Logging centralized log collection
- Log Router pipeline from Cloud Logging to BigQuery
- SQL-based log analytics and health classification
- Application health score and performance metrics
- Interactive Looker Studio monitoring dashboard

## Health Metrics

The system analyzes:

- Total requests
- Successful requests
- HTTP 4xx failures
- HTTP 5xx server errors
- Abnormal requests
- Success rate
- Error rate
- Average latency
- P95 latency
- Overall application health score

## Tech Stack

Python | Flask | Google Cloud Run | Cloud Logging | Log Router | BigQuery | Looker Studio | SQL | Gunicorn

## Project Structure

cloud-log-app/
├── main.py
├── traffic_generator.py
├── requirements.txt
├── templates/
├── static/
└── sql/
    └── analytics_views.sql

## How It Works

1. The Flask application runs as a containerized serverless service on Cloud Run.
2. Application and HTTP request events are captured by Cloud Logging.
3. Log Router exports relevant Cloud Run logs to BigQuery.
4. BigQuery SQL transforms raw request logs into analytics metrics.
5. Requests are classified as healthy, failed, critical or anomalous.
6. Looker Studio visualizes application health and performance.
7. A Python traffic generator simulates realistic request patterns for testing.

## Dashboard

The monitoring dashboard provides application health KPIs, request-status distribution, request activity over time, error analysis and detailed request logs.

## Author

Deandra Fernandes
B.Tech Electrical and Computer Engineering
MIT-WPU, Pune
