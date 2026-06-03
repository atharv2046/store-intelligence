from pydantic import BaseModel
from typing import Optional, Dict
from uuid import uuid4

class Event(BaseModel):
    event_id: str
    store_id: str
    camera_id: str
    visitor_id: str
    event_type: str
    timestamp: str

    zone_id: Optional[str] = None
    dwell_ms: Optional[int] = 0
    is_staff: bool = False
    confidence: float = 1.0

    metadata: Dict = {}