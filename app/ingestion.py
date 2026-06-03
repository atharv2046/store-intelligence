from typing import List

event_store = {}

def ingest_events(events):
    accepted = []
    rejected = []

    for event in events:
        if event.event_id in event_store:
            continue

        try:
            event_store[event.event_id] = event
            accepted.append(event.event_id)
        except Exception:
            rejected.append(event.event_id)

    return {
        "accepted": len(accepted),
        "rejected": len(rejected)
    }

def get_all_events():
    return list(event_store.values())