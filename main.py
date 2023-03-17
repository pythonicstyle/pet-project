from aiogram.utils import executor

from utils.bot_commands import set_default_commands
from loader import dp, bot
from database import sqlite_db
from handlers import callback_handlers, default_handlers


async def on_startup(_) -> None:
    await sqlite_db.db_connect()
    print("Bot has been started up")
    print("DataBase is connected")


if __name__ == '__main__':
    async def start_bot_commands_menu() -> None:
        await set_default_commands(bot)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
