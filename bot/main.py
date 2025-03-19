import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from bot.handlers import start, survey, ai_chat, bitrix
from bot.db.db import init_db

# Проверка переменных окружения
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден. Проверьте .env файл.")

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создание экземпляра бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def register_handlers():
    """Функция регистрации всех обработчиков бота"""
    dp.include_router(start.router)
    dp.include_router(survey.router)
    dp.include_router(ai_chat.router)
    dp.include_router(bitrix.router)


async def main():
    """Главная асинхронная функция для запуска бота"""
    init_db()  # Инициализация базы данных
    register_handlers()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
