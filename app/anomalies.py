def detect_anomalies(metrics):

    anomalies = []

    if metrics["unique_visitors"] == 0:
        anomalies.append({
            "severity": "WARN",
            "type": "DEAD_STORE"
        })

    return anomalies