from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text

from loader import dp


@dp.message_handler(Text(equals='✖️ close keyboard'))
async def close_command(message: types.Message) -> None:
    """ Функция обрабатывает запрос и закрывает меню """
    await message.answer(text="Вы закрыли меню",
                         reply_markup=ReplyKeyboardRemove())
