from datetime import datetime
from aiogram import types
import logging

from keyboards.buttons import main_menu_kb
from loader import bot, dp

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message) -> None:
    """
    Функция обрабатывает команду запуска бота,
    выводит пользователю приветствие и главное меню
    """
    user_id = message.from_user.id
    user_fullname = message.from_user.full_name
    greeting = f"<b>Здравствуйте, {message.from_user.first_name}!</b>"
    await bot.send_message(message.from_user.id,
                           text=f"{greeting}\nВыберите дальнейшее действие из меню или введите 4-х буквенный код аэропорта, например <b>UUEE</b>",
                           reply_markup=main_menu_kb())
    logging.info(f"{user_id=} {user_fullname=} - {datetime.now()}")
