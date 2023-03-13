from loader import dp
from aiogram import types
from aiogram.types import ReplyKeyboardRemove


@dp.message_handler(commands=['close'])
async def close_command(message: types.Message) -> None:
    await message.answer(text="Клавиатура отключена",
                         reply_markup=ReplyKeyboardRemove())
