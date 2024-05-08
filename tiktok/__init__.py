import os
from dotenv import load_dotenv
load_dotenv()

APP_ID = os.getenv("TIKTOK_APP_ID")
APP_SECRET = os.getenv("TIKTOK_APP_SECRET")
SANBOX_ACCESS_TOKEN = os.getenv('TIKTOK_SANDBOX_ACCESS_TOKEN')
ENV = os.getenv('ENV')