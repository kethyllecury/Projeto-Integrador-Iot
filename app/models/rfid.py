from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class RfidPayload(BaseModel):
    uid: str = Field(..., description="UID do cartão RFID")
    tag_type: Optional[str] = None
    rssi: Optional[int] = None
    timestamp: Optional[str] = None
    extra: Optional[Dict[str, Any]] = None
