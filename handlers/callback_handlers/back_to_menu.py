from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from loader import dp
from keyboards.buttons import main_menu_kb


@dp.message_handler(Text(equals="📌 main menu"), state='*')
async def return_menu(message: types.Message, state: FSMContext) -> None:
    """
    Функция обрабатывает сообщение пользователя и
    отменяет машину состояний и возвращает пользователю главное меню
    """
    if state is None:
        return
    await state.finish()
    await message.answer(text="Вы вернулись в главное меню",
                         reply_markup=main_menu_kb())
