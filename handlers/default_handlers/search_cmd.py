from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp
from keyboards.inline_buttons import city_menu_ikb


@dp.message_handler(Text(equals='🔎 search'))
async def search_command(message: types.Message) -> None:
    """ Функция обрабатывает запрос пользователя и выводит стандартное меню городов """
    await message.answer(text="Выберите город",
                         reply_markup=city_menu_ikb())
