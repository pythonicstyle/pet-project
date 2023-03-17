from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp
from keyboards.custom_inline_buttons import custom_menu_ikb


@dp.message_handler(Text(equals="⚙️ custom menu"))
async def custom_cmd(message: types.Message) -> None:
    """ Функция обрабатывает запрос и открывает пользователю дополнительное меню для настройки """
    await message.answer("Выберите действие из меню",
                         reply_markup=custom_menu_ikb())
