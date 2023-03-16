import sqlite3
from typing import List


async def db_connect() -> None:
    global base, cursor
    base = sqlite3.connect('database/custom_menu.db')
    cursor = base.cursor()
    base.execute("CREATE TABLE IF NOT EXISTS custom (key_number INTEGER PRIMARY KEY, city TEXT, airport TEXT)")
    base.commit()


async def get_custom_menu() -> List:
    data = cursor.execute("SELECT * FROM custom").fetchall()
    return data


async def create_custom_menu(state):
    async with state.proxy() as data:
        custom_info = cursor.execute("INSERT INTO custom (city, airport) VALUES (?, ?)", (data['city'], data['airport']))
        base.commit()
    return custom_info


async def delete_city_from_custom_menu(key_number: int) -> None:
    cursor.execute("DELETE FROM custom WHERE key_number = ?", key_number)
    base.commit()
