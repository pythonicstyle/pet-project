import sqlite3


async def db_start():
    global base, cursor
    base = sqlite3.connect('../database/request_history.db')
    cursor = base.cursor()
    base.execute("CREATE TABLE IF NOT EXISTS log_data (user_id TEXT, user_name TEXT, code TEXT, request_time TEXT)")
    base.commit()


# async def create_data(user_id):
#     user = cursor.execute(f"SELECT 1 FROM log_data WHERE user_id == {user_id}").fetchone()
#     if not user:
#         cursor.execute("INSERT INTO log_data VALUES(?, ?, ?, ?)", (user_id, user_name, '', ''))
#         base.commit()


async def edit_data(state, user_id):
    async with state.proxy() as data:
        cursor.execute(f"UPDATE log_data SET user_name = {data['name']}, code = {data['code']}, request_time = {data['time']} WHERE user_id == {user_id}")
        base.commit()