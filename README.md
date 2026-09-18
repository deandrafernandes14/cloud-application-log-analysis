# ☁️ Cloud Application Log Analysis System

A cloud-native application monitoring and log analytics system built on **Google Cloud Platform (GCP)**.

The system collects application logs, identifies **errors, failed requests, abnormal activity, and latency issues**, analyzes the logs using BigQuery, and generates an interactive dashboard summarizing overall application health.

---

## 🚀 Live Project

🌐 **[Open Live Application](https://cloud-log-analysis-207601808748.asia-south1.run.app)**

📊 **[Open Interactive Looker Studio Dashboard](https://datastudio.google.com/reporting/048c6687-ed82-49c7-8992-bf931b2345b8)**

---

## 📊 Application Health Dashboard

The Looker Studio dashboard visualizes application health, request behaviour, errors, anomalies, and latency metrics derived from Cloud Run logs.

<img width="727" height="338" alt="Cloud Application Health Dashboard" src="https://github.com/user-attachments/assets/5f0a092e-9806-4d7d-becd-d724e16c0e41" />

<img width="719" height="369" alt="Application Log Analytics Dashboard" src="https://github.com/user-attachments/assets/b0b3552e-b8b7-40b6-9f2c-44d6ae27910d" />

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
┌─────────────────────────┐
│    Google Cloud Run     │
│     Flask Application   │
└────────────┬────────────┘
             │
             │ Application + HTTP Logs
             ▼
┌─────────────────────────┐
│      Cloud Logging      │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│     Log Router Sink     │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│        BigQuery         │
│      SQL Analytics      │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│      Looker Studio      │
│   Health Dashboard      │
└─────────────────────────┘
```

**Data Flow:**  
`User / Traffic Generator → Cloud Run → Cloud Logging → Log Router → BigQuery → Looker Studio`

---

## ✨ Key Features

- Serverless Flask application deployed on Google Cloud Run
- Automatic application and HTTP request logging
- Centralized log collection using Cloud Logging
- Log Router pipeline from Cloud Logging to BigQuery
- HTTP 4xx failed-request detection
- HTTP 5xx server-error detection
- Abnormal activity monitoring
- Request latency analysis
- P95 latency calculation
- Success and error-rate calculation
- Application health scoring
- Automated traffic simulation
- SQL-based log analytics
- Interactive Looker Studio dashboard

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Application | Python, Flask |
| Frontend | HTML, CSS |
| Deployment | Google Cloud Run |
| Logging | Google Cloud Logging |
| Log Routing | Cloud Logging Log Router |
| Analytics | Google BigQuery |
| Query Language | SQL |
| Visualization | Looker Studio |
| Traffic Simulation | Python |
| Version Control | Git, GitHub |
| Cloud Platform | Google Cloud Platform |

---

## ⚙️ How the System Works

1. The **Flask application** is deployed as a serverless service on Google Cloud Run.

2. Users and the automated traffic generator send HTTP requests to the application.

3. Cloud Run request logs and application events are automatically captured by **Cloud Logging**.

4. A **Cloud Logging Log Router sink** exports the relevant logs to **BigQuery**.

5. **BigQuery SQL views** transform the collected logs into request-health and system-health metrics.

6. **Looker Studio** connects to the BigQuery analytics views and displays application health through an interactive dashboard.

---

## 🧪 Automated Traffic Simulation

The project includes `traffic_generator.py` to generate application activity and test the complete monitoring pipeline.

The generator produces a mixture of:

- Successful requests
- Failed requests
- Server errors
- Slow requests
- Abnormal activity

Run the traffic generator using:

```bash
python traffic_generator.py "YOUR_CLOUD_RUN_URL"
```

This creates request data for testing the logging, analytics, and visualization pipeline.

---

## 🔎 Cloud Logging

Cloud Run automatically sends application and HTTP request logs to **Google Cloud Logging**.

The deployed service can be located in Logs Explorer using:

```text
resource.type="cloud_run_revision"
resource.labels.service_name="cloud-log-analysis"
```

Relevant Cloud Run logs are exported through a **Log Router sink** to BigQuery for analysis.

---

## 🗄️ BigQuery Analytics

The project uses three analytics views to transform collected log data into useful monitoring information.

### `application_health`

Provides request-level information including:

- Timestamp
- Request URL
- HTTP method
- HTTP status
- Health status

Requests are classified into categories such as:

`HEALTHY` • `ERROR` • `FAILED` • `ABNORMAL`

### `request_analytics`

Provides request-level analytics for studying application activity and performance.

### `system_health`

Calculates aggregated application-health KPIs including:

- Total requests
- Successful requests
- Failed requests
- Server errors
- Anomalies
- Average latency
- P95 latency
- Success rate
- Error rate
- Failure rate
- Anomaly rate
- Health score
- Overall system status

The SQL definitions used to create these analytics views are available in:

```text
sql/analytics_views.sql
```

---

## 📈 Dashboard Components

The Looker Studio dashboard contains:

### KPI Cards

`Total Requests` • `Health Score` • `Error Rate` • `Success Rate` • `P95 Latency`

### Request Health Distribution

Visualizes the distribution of healthy, failed, erroneous, and abnormal requests.

### Request Activity Over Time

Displays application request activity and health events over time.

### Health Status Analysis

Compares request counts across different health categories.

### Request Details

Displays request-level information including timestamp, health status, HTTP status, and requested URL.

📊 **[View Interactive Dashboard](https://datastudio.google.com/reporting/048c6687-ed82-49c7-8992-bf931b2345b8)**

---

## 📁 Project Structure

```text
cloud-application-log-analysis/
│
├── main.py
├── traffic_generator.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── sql/
    └── analytics_views.sql
```

---

## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/deandrafernandes14/cloud-application-log-analysis.git
cd cloud-application-log-analysis
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python main.py
```

---

## ☁️ Deploy to Google Cloud Run

```bash
gcloud run deploy cloud-log-analysis \
  --source . \
  --region asia-south1 \
  --allow-unauthenticated
```

The application is deployed in the **asia-south1** Google Cloud region.

---

## 🎯 Project Objective

The objective of this project is to develop a cloud-based system that **collects application logs and analyzes them to identify errors, failed requests, and abnormal activity while generating a dashboard summarizing application health**.

The project demonstrates an end-to-end cloud observability workflow:

**Serverless Deployment → Centralized Logging → Log Routing → SQL Analytics → Interactive Visualization**

---

## 🔮 Future Enhancements

- Structured JSON application logging
- Cloud Monitoring alerts
- Log-based metrics
- Automated alerts for high error rates
- Service Level Objectives (SLOs)
- Real-time streaming analytics
- Machine-learning-based anomaly detection
- Authentication and role-based access

---

## 👩‍💻 Author

**Deandra Fernandes**  
B.Tech Electrical and Computer Engineering  
MIT World Peace University, Pune

**GitHub:** [deandrafernandes14](https://github.com/deandrafernandes14)

