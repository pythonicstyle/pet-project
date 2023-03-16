from loader import dp
from aiogram import types
from keyboards.inline_buttons import city_menu_ikb
from aiogram.dispatcher.filters import Text


@dp.message_handler(Text(equals='🔎 search'))
async def search_command(message: types.Message) -> None:
    await message.answer(text="Выберите город",
                         reply_markup=city_menu_ikb())
