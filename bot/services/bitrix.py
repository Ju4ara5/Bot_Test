import requests
from bot.config import BITRIX_WEBHOOK


def create_bitrix_deal(data: dict):
    url = f"{BITRIX_WEBHOOK}/crm.deal.add"
    response = requests.post(url, json={"fields": data})
    return response.json()
