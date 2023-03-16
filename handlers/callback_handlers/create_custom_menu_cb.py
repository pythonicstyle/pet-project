from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from database import sqlite_db
from keyboards.buttons import cancel_kb
from keyboards.custom_inline_buttons import custom_menu_ikb

from loader import dp
from aiogram import types


class CustomMenuStates(StatesGroup):

    city = State()
    airport = State()


@dp.callback_query_handler(text="create_new_menu")
async def input_custom_menu_data(callback: types.CallbackQuery) -> None:
    await callback.message.delete()
    await callback.message.answer("Введите название города",
                                  reply_markup=cancel_kb())
    await CustomMenuStates.city.set()
    await callback.answer()


@dp.message_handler(state=CustomMenuStates.city)
async def handle_city(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['city'] = message.text
    await message.reply("Теперь введите 4-х буквенный код ИКАО аэропорта",
                        reply_markup=cancel_kb())
    await CustomMenuStates.next()


@dp.message_handler(state=CustomMenuStates.airport)
async def handle_airport(message: types.Message, state: FSMContext) -> None:
    if len(message.text) == 4 and message.text.isalpha():
        async with state.proxy() as data:
            data['airport'] = message.text.upper()
        await sqlite_db.create_custom_menu(state)
        await message.reply("Аэропорт добавлен в меню!",
                            reply_markup=custom_menu_ikb())
        await state.finish()
    else:
        await message.answer("Код аэропорта должен состоять их 4-х латинских букв.")
