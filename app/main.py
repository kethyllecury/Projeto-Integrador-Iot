from fastapi import FastAPI
from app.routes.rfid_routes import router as rfid_router

app = FastAPI(title="RFID Backend com MongoDB Atlas")
app.include_router(rfid_router)
