from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Text

DESCRIPTION = ("🔹 Чтобы получить информацию о фактической погоде на аэродроме, "
               "введите 4-х буквенную аббревиатуру аэропорта или воспользуйтесь командой '🔎 search'\n"
               "------------------------------------\n"
               "🔹 Если вы хотите узнать аббревиатуру, "
               "или посмотреть список аэропортов, нажмите команду '🆘 help'\n"
               "------------------------------------\n"
               "🔹 Чтобы создать меню из своих городов, воспользуйтесь командой '⚙️ custom menu'\n"
               "------------------------------------\n"
               "🔹 Чтобы отключить клавиатуру, нажмите '✖️ close keyboard'\n")


@dp.message_handler(Text(equals="📎 description"))
async def description_command(message: types.Message) -> None:
    await message.answer(text=DESCRIPTION)
