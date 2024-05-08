import os
from dotenv import load_dotenv
load_dotenv()

APP_ID = os.getenv("TIKTOK_APP_ID")
APP_SECDRET = os.getenv("TIKTOK_APP_SECRET")
SANDBOX_ACCESS_TOKEN = os.getenv('TIKTOK_SANDBOX_ACCESS_TOKEN')
ACCESS_TOKEN = os.getenv('TIKTOK_ACCESS_TOKEN')
ENV = os.getenv('ENV')