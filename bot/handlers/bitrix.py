import requests
import os

BITRIX_WEBHOOK = os.getenv("BITRIX_WEBHOOK")


async def create_or_update_deal(data):
    """Создание или обновление сделки в Bitrix24"""
    deal_data = {
        "fields": {
            "TITLE": f"Сделка с {data['name']}",
            "PHONE": [{"VALUE": data["phone"], "VALUE_TYPE": "WORK"}],
            "EMAIL": [{"VALUE": data["email"], "VALUE_TYPE": "WORK"}]
        }
    }

    url = f"{BITRIX_WEBHOOK}/crm.deal.add"
    response = requests.post(url, json=deal_data)
    return response.json()


async def save_chat_history(user_id, user_message, bot_response):
    """Сохранение истории чатов в Bitrix24"""
    chat_data = {
        "fields": {
            "USER_ID": user_id,
            "USER_MESSAGE": user_message,
            "BOT_RESPONSE": bot_response
        }
    }

    url = f"{BITRIX_WEBHOOK}/crm.timeline.comment.add"
    requests.post(url, json=chat_data)
