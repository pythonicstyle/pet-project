from aiogram.types import BotCommand
from config_data.config import DEFAULT_COMMANDS


async def set_default_commands(bot):
    for i in DEFAULT_COMMANDS:
        await bot.set_my_commands(BotCommand(*i))
