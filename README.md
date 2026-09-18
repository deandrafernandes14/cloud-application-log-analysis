# ☁️ Cloud Application Log Analysis System

A cloud-native application monitoring and log analytics system built on **Google Cloud Platform (GCP)**.

The system collects application logs, identifies **errors, failed requests, abnormal activity, and latency issues**, analyzes the logs using BigQuery, and generates an interactive dashboard summarizing overall application health.

## 🚀 Live Project

🌐 **[Open Live Application](https://cloud-log-analysis-207601808748.asia-south1.run.app)**

📊 **[Open Interactive Looker Studio Dashboard](https://datastudio.google.com/reporting/048c6687-ed82-49c7-8992-bf931b2345b8)**

---

## 📊 Application Health Dashboard

The Looker Studio dashboard provides real-time visualization of application health and request analytics.

<img width="727" height="338" alt="image" src="https://github.com/user-attachments/assets/5f0a092e-9806-4d7d-becd-d724e16c0e41" />
<img width="719" height="369" alt="image" src="https://github.com/user-attachments/assets/b0b3552e-b8b7-40b6-9f2c-44d6ae27910d" />


### Key Metrics

- Total Requests
- Health Score
- Success Rate
- Error Rate
- P95 Request Latency
- Failed Requests
- Server Errors
- Abnormal Activity

---

## 🏗️ System Architecture

```text
User / Traffic Generator
          │
          ▼
┌─────────────────────┐
│  Google Cloud Run   │
│  Flask Application  │
└──────────┬──────────┘
           │
           │ Application & HTTP Logs
           ▼
┌─────────────────────┐
│   Cloud Logging     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Log Router Sink    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      BigQuery       │
│   SQL Analytics     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    Looker Studio    │
│  Health Dashboard   │
└─────────────────────┘


