from app.models.rfid import RfidPayload
from app.core.database import collection
from app.etl.rfid_etl import clean_rfid_data


def insert_rfid_reading(payload: RfidPayload):
    transformed = clean_rfid_data(payload.dict())

    result = collection.insert_one(transformed)
    return result


def get_latest_readings(n: int = 10):
    docs = list(collection.find().sort("_id", -1).limit(n))
    for doc in docs:
        doc["_id"] = str(doc["_id"])
    return docs
