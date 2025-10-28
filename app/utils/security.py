from fastapi import Header, HTTPException
from app.core.config import API_KEY
from typing import Optional

def verify_api_key(x_api_key: Optional[str] = Header(None)):
    if not x_api_key or x_api_key.strip() != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API Key")
