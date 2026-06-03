from fastapi import FastAPI
from typing import List

from app.models import Event
from app.ingestion import ingest_events

app = FastAPI(title="Store Intelligence API")

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/events/ingest")
def ingest(events: List[Event]):
    return ingest_events(events)