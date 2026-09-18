-- Cloud Application Log Analysis System
-- BigQuery analytics layer

-- Request-level analytics
CREATE OR REPLACE VIEW `cloud-log-analysis-deandra.log_analysis.request_analytics` AS
SELECT
  timestamp,
  httpRequest.requestMethod AS method,
  httpRequest.requestUrl AS request_url,
  httpRequest.status AS status,
  CASE
    WHEN httpRequest.status >= 500 THEN 'CRITICAL'
    WHEN httpRequest.status >= 400 THEN 'WARNING'
    WHEN REGEXP_CONTAINS(httpRequest.requestUrl, r'slow') THEN 'ANOMALY'
    ELSE 'HEALTHY'
  END AS health_status
FROM
  `cloud-log-analysis-deandra.log_analysis.run_googleapis_com_requests`;
