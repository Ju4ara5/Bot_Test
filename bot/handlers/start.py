from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def start_command(message: types.Message):
    """Обработчик команды /start"""
    await message.answer("Привет! Я Telegram-бот. Давайте начнем анкетирование!")
