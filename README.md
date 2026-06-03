# Store Intelligence System

## Overview

Store Intelligence System is a retail analytics platform that uses CCTV video feeds to generate business insights about customer behavior inside a store.

The system detects and tracks customers using computer vision techniques and provides metrics such as visitor count, section-wise traffic, dwell time, queue monitoring, and conversion funnel analytics.

---

## Features

### Visitor Analytics

* Total visitor count
* Entry and exit monitoring
* Unique visitor tracking

### Zone Analytics

* Section-wise visitor count
* Percentage of visitors per section
* Customer movement tracking

### Dwell Time Analysis

* Average dwell time per section
* Customer engagement measurement

### Queue Monitoring

* Billing queue estimation
* Queue depth monitoring
* Queue spike detection

### Dashboard

* Real-time analytics dashboard
* KPI visualization
* Section-wise traffic reports

### API Services

* Event ingestion API
* Metrics API
* Funnel analytics API

---

## Project Architecture

```text
CCTV Videos
      |
      v
YOLOv8 Person Detection
      |
      v
Object Tracking
      |
      v
Event Generation
      |
      v
FastAPI Backend
      |
      v
Analytics Engine
      |
      v
Streamlit Dashboard
```

---

## Project Structure

```text
store-intelligence/

├── config.json

├── detect.py
├── tracker.py
├── emit.py

├── videos/
│   ├── store1/
│   └── store2/

├── app/
│   ├── main.py
│   ├── models.py
│   ├── ingestion.py
│   ├── metrics.py
│   ├── funnel.py
│   └── anomalies.py

├── dashboard/
│   └── app.py

├── output/

├── requirements.txt
├── Dockerfile
├── docker-compose.yml

├── README.md
├── DESIGN.md
└── CHOICES.md
```

---

## Technologies Used

### Backend

* FastAPI
* Python
* Pydantic

### Computer Vision

* YOLOv8
* OpenCV

### Dashboard

* Streamlit

### Data Processing

* Pandas
* NumPy

### Testing

* Pytest

### Containerization

* Docker

---

## Installation

### Clone Repository

```bash
git clone https://github.com/atharv2046/store-intelligence.git
cd store-intelligence
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Start FastAPI Server

```bash
python -m uvicorn app.main:app --reload
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

### Run Detection Pipeline

```bash
python detect.py
```

---

### Run Dashboard

```bash
python -m streamlit run dashboard/app.py
```

Dashboard URL:

```text
http://localhost:8501
```

---

## Analytics Provided

### Visitor Metrics

* Total Visitors
* Entry Count
* Exit Count

### Zone Metrics

* Visitors in Zone 1
* Visitors in Zone 2
* Visitors in Billing Area

### Engagement Metrics

* Average Dwell Time
* Section Popularity

### Queue Metrics

* Queue Depth
* Queue Alerts

### Conversion Funnel

```text
Entered Store
      ↓
Visited Section
      ↓
Reached Billing
      ↓
Purchase
```

---

## Sample Output

```json
{
  "total_visitors": 100,
  "zone_1_visitors": 70,
  "zone_2_visitors": 45,
  "billing_visitors": 30,
  "avg_dwell_time": 95
}
```

---

## Future Enhancements

* Multi-camera synchronization
* Person re-identification
* Real-time video streaming
* POS transaction integration
* Heatmap generation
* Cloud deployment

---

## Author

Atharv

GitHub:
https://github.com/atharv2046
