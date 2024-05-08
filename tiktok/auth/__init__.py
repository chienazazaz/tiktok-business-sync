import os 
from dotenv import load_dotenv
load_dotenv()

APP_ID = os.getenv("TIKTOK_APP_ID")
APP_SECDRET = os.getenv("TIKTOK_APP_SECRET")