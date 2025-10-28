from datetime import datetime
from app.core.database import collection
from app.models.rfid import RfidPayload

def insert_rfid_reading(payload: RfidPayload):
    doc = payload.dict()
    doc["timestamp"] = payload.timestamp or datetime.utcnow().isoformat()
    doc["received_at"] = datetime.utcnow().isoformat()
    return collection.insert_one(doc)

def get_latest_readings(n: int = 10):
    docs = list(collection.find().sort("_id", -1).limit(n))
    for doc in docs:
        doc["_id"] = str(doc["_id"])
    return docs
