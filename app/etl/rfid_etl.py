from datetime import datetime
from typing import Dict, Any

def clean_rfid_data(data: Dict[str, Any]) -> Dict[str, Any]:
    cleaned = data.copy()

   
    if "uid" in cleaned:
        cleaned["uid"] = cleaned["uid"].strip().upper()

    if "rssi" in cleaned and cleaned["rssi"] is not None:
        try:
            cleaned["rssi"] = int(cleaned["rssi"])
        except ValueError:
            cleaned["rssi"] = None

    if "timestamp" not in cleaned or not cleaned["timestamp"]:
        cleaned["timestamp"] = datetime.utcnow().isoformat()

    cleaned["processed_at"] = datetime.utcnow().isoformat()

    return cleaned
