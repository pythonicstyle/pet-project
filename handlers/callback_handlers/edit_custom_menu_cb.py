from aiogram import types
from aiogram.utils.callback_data import CallbackData

from database import sqlite_db
from loader import dp


delete_city_cb = CallbackData('city', 'id', 'action')


@dp.callback_query_handler(delete_city_cb.filter(action='delete'))
async def delete_city(callback: types.CallbackQuery, callback_data: dict) -> None:
    """ Функция обрабатывает callback запрос удаления элемента из базы данных """
    await sqlite_db.delete_city_from_custom_menu(callback_data['id'])
    await callback.message.delete()
    await callback.answer()
