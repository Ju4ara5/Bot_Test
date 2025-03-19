"""
AI-диалог с GPT-4
"""
import os
import openai
from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.handlers.bitrix import save_chat_history

router = Router()

openai.api_key = os.getenv("OPENAI_API_KEY")


@router.message()
async def ai_chat(message: types.Message, state: FSMContext):
    """AI-диалог с возможностью отправки ссылок и видео"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": message.text}]
    )

    reply = response["choices"][0]["message"]["content"]

    # Inline-кнопки
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Связаться с менеджером", callback_data="contact_manager")
    keyboard.button(text="Перейти к оплате", url="https://example.com/payment")
    keyboard.button(text="Дополнительный вопрос", callback_data="ask_more")
    keyboard.adjust(1)

    await message.answer(reply, reply_markup=keyboard.as_markup())

    # Сохранение переписки в Bitrix24
    await save_chat_history(message.from_user.id, message.text, reply)
