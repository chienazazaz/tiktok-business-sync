import os
from dotenv import load_dotenv
load_dotenv()

SANDBOX_ACCESS_TOKEN = os.getenv('TIKTOK_SANDBOX_ACCESS_TOKEN')
ACCESS_TOKEN = os.getenv('TIKTOK_ACCESS_TOKEN')
ENV = os.getenv('ENV')