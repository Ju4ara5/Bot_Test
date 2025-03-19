import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from bot.handlers import start, survey, ai_chat, bitrix

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создание бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def register_handlers():
    """Регистрация всех обработчиков бота"""
    dp.include_router(start.router)
    dp.include_router(survey.router)
    dp.include_router(ai_chat.router)
    dp.include_router(bitrix.router)


async def main():
    """Запуск бота"""
    register_handlers()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
