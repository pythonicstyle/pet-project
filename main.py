from aiogram.utils import executor
from utils.bot_commands import set_default_commands
from loader import dp, bot
from database import sqlite_db


async def on_startup(_):
    # await sqlite_db.db_start()
    print("Bot has been started up")
    print("DataBase is connected")


if __name__ == '__main__':
    async def start_bot_commands_menu():
        await set_default_commands(bot)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
