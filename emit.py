import uuid
from datetime import datetime

def emit_event(
        store_id,
        visitor_id,
        event_type,
        zone_id=None):

    return {
        "event_id": str(uuid.uuid4()),
        "store_id": store_id,
        "visitor_id": visitor_id,
        "event_type": event_type,
        "timestamp": datetime.utcnow().isoformat(),
        "zone_id": zone_id
    }