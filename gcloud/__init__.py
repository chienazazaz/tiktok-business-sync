import os
from dotenv import load_dotenv

load_dotenv()

PUBLIC_URL = os.getenv("PUBLIC_URL")
QUEUE = os.getenv("QUEUE")
LOCATION = os.getenv("LOCATION")
DATASET = os.getenv("DATASET")
PROJECT_ID = os.getenv("PROJECT_ID")
SERVICE_ACCOUNT = os.getenv("SERVICE_ACCOUNT")
