from fastapi import APIRouter, Depends
from app.models.rfid import RfidPayload
from app.utils.security import verify_api_key
from app.services.rfid_service import insert_rfid_reading, get_latest_readings

router = APIRouter(prefix="/api", tags=["RFID"])

@router.post("/rfid", status_code=201)
async def receive_rfid(payload: RfidPayload, _: None = Depends(verify_api_key)):
    result = insert_rfid_reading(payload)
    return {"status": "ok", "id": str(result.inserted_id), "uid": payload.uid}

@router.get("/readings/latest")
async def latest_readings(n: int = 10, _: None = Depends(verify_api_key)):
    return get_latest_readings(n)
