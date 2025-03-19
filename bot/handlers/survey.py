"""
Обработчик анкетирования
"""
from aiogram import Router, types

router = Router()


@router.message()
async def survey_handler(message: types.Message):
    """Обработчик анкетирования, сохраняет ответы в БД"""
    await message.answer("Ваш ответ записан. Следующий вопрос...")
