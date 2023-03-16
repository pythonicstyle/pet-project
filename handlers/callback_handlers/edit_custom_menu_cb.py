from database import sqlite_db
from loader import dp
from aiogram import types
from aiogram.utils.callback_data import CallbackData


delete_city_cb = CallbackData('city', 'id', 'action')


@dp.callback_query_handler(delete_city_cb.filter(action='delete'))
async def delete_city(callback: types.CallbackQuery, callback_data: dict) -> None:
    await sqlite_db.delete_city_from_custom_menu(callback_data['id'])
    await callback.message.delete()
    await callback.answer()
