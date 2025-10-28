from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "meubanco")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "api")

if not MONGO_URI:
    raise RuntimeError("MONGO_URI não configurado no .env")
