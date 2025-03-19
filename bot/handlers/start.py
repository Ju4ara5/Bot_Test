from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()


@router.message(Command("start"))
async def start_command(message: types.Message):
    """Обработчик команды /start"""
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Компания", callback_data="category_company")
    keyboard.button(text="Частное лицо", callback_data="category_individual")
    keyboard.adjust(2)

    await message.answer(
        "Добро пожаловать! Выберите категорию:",
        reply_markup=keyboard.as_markup()
    )


@router.callback_query(lambda c: c.data.startswith("category_"))
async def category_selected(callback: types.CallbackQuery):
    """Обработчик выбора категории"""
    category = "Компания" if callback.data == "category_company" else "Частное лицо"
    await callback.message.answer(f"Вы выбрали: {category}. Начнем анкетирование.")
    await callback.message.answer("Введите ваше имя:")
    await callback.answer()
