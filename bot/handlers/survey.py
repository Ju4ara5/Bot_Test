"""
Обработчик анкетирования
"""
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from bot.db.db import save_user_data
from bot.handlers.bitrix import create_or_update_deal

router = Router()


class Survey(StatesGroup):
    name = State()
    phone = State()
    email = State()


@router.message(F.text, Survey.name)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите ваш телефон:")
    await state.set_state(Survey.phone)


@router.message(F.text, Survey.phone)
async def get_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Введите ваш email:")
    await state.set_state(Survey.email)


@router.message(F.text, Survey.email)
async def get_email(message: types.Message, state: FSMContext):
    data = await state.update_data(email=message.text)

    # Сохранение в БД
    await save_user_data(message.from_user.id, data["name"], data["phone"], data["email"], "Компания")

    # Создание сделки в Bitrix24
    await create_or_update_deal(data)

    await message.answer("Спасибо! Теперь вы можете задать любой вопрос.")
