from loader import dp
from aiogram import types

DESCRIPTION = ("Чтобы получить информацию о фактической погоде на аэродроме, "
               "введите 4-х буквенную аббревиатуру аэропорта. Если вы хотите узнать аббревиатуру, "
               "или посмотреть список аэропортов, нажмите команду /help")


@dp.message_handler(commands=["description"])
async def description_command(message: types.Message) -> None:
    await message.answer(text=DESCRIPTION)
