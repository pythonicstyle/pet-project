from loader import dp
from aiogram import types
from keyboards.inline_buttons import city_menu_ikb


@dp.message_handler(commands=['search'])
async def search_command(message: types.Message) -> None:
    await message.answer(text="Выберите город",
                         reply_markup=city_menu_ikb())
