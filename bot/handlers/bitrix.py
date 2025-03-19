from aiogram import Router, types

router = Router()


@router.message()
async def bitrix_handler(message: types.Message):
    """Обработчик для работы с Bitrix24"""
    await message.answer("Информация отправлена в CRM Bitrix24!")
