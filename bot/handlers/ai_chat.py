"""
AI-диалог с GPT-4
"""
from aiogram import Router, types

router = Router()


@router.message()
async def ai_chat_handler(message: types.Message):
    """Обработчик сообщений для AI-диалога"""
    await message.answer("[AI] Ответ на ваш вопрос...")
