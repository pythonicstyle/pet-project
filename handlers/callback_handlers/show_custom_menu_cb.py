from aiogram import types

from keyboards.custom_inline_buttons import create_custom_button_ikb, custom_menu_ikb
from database import sqlite_db
from loader import dp, bot


async def show_custom_menu(callback: types.CallbackQuery, menu: list) -> None:
    """
    Функция обрабатывает callback запрос и
    преобразовывает полученный список кортежей для вывода информации пользователю
    """
    for line in menu:
        await bot.send_message(callback.from_user.id,
                               text=f"📍:  <b>{line[1]}</b> \n"
                                    f"🔑:  <b>{line[2]}</b>",
                               reply_markup=create_custom_button_ikb(line))


@dp.callback_query_handler(text="show_custom_menu")
async def get_custom_menu(callback: types.CallbackQuery) -> None:
    """
    Функция обрабатывает callback запрос, обращается к базе данных,
    откуда достает всю информацию и передает ее в функцию show_custom_menu
    """
    menu = await sqlite_db.get_custom_menu()
    if not menu:
        await callback.message.answer("Пока в меню ничего нет ☹️",
                                      reply_markup=custom_menu_ikb())
        await callback.message.delete()

    await show_custom_menu(callback, menu)
    await callback.answer()
