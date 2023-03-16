from loader import dp
from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text


@dp.message_handler(Text(equals='✖️ close keyboard'))
async def close_command(message: types.Message) -> None:
    await message.answer(text="Клавиатура отключена",
                         reply_markup=ReplyKeyboardRemove())
