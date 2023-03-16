from aiogram import types
from keyboards.custom_inline_buttons import custom_menu_ikb
from loader import dp
from aiogram.dispatcher.filters import Text


@dp.message_handler(Text(equals="⚙️ custom menu"))
async def custom_cmd(message: types.Message) -> None:
    await message.answer("Выберите действие из меню",
                         reply_markup=custom_menu_ikb())
