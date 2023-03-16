from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from keyboards.buttons import main_menu_kb
from aiogram.dispatcher.filters import Text


@dp.message_handler(Text(equals="📌 main menu"), state='*')
async def return_menu(message: types.Message, state: FSMContext) -> None:
    if state is None:
        return
    await state.finish()
    await message.answer(text="Вы вернулись в главное меню",
                         reply_markup=main_menu_kb())
