from loader import dp
from aiogram import types
from keyboards.buttons import main_menu_kb


@dp.message_handler(commands=["history"])
async def history_command(message: types.Message) -> None:
    await message.answer("пока тут заглушка ☹️",
                         reply_markup=main_menu_kb())
