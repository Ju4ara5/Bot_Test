import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DB_URL = os.getenv("DB_URL")
BITRIX_WEBHOOK = os.getenv("BITRIX_WEBHOOK")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
