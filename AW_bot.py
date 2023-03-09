import requests
from datetime import datetime
from aiogram import types
from aiogram.utils import executor
import logging

from main import dp, bot
from config import API_KEY
from keyboards.inline_buttons import help_menu

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message) -> None:
    user_id = message.from_user.id
    user_fullname = message.from_user.full_name
    greeting = f"<b>Привет, {message.from_user.first_name}!</b>"
    await bot.send_message(message.from_user.id,
                           text=f"{greeting}\nВыберете дальнейшее действие из меню или введите 4-х буквенный код аэропорта,например,  <b>uuee</b>")
    logging.info(f"{user_id=} {user_fullname} - {datetime.today()}")


@dp.message_handler(commands=["help"])
async def help_command(message: types.Message) -> None:
    await bot.send_message(message.from_user.id,
                           "- Посмотреть таблицу с расшифровкой всех символов - выберите таблицу\n"
                           "- Посмотреть код ИКАО желаемого аэропорта - выберите список",
                           reply_markup=help_menu)


@dp.message_handler(commands=["description"])
async def description_command(message: types.Message) -> None:
    await bot.send_message(message.from_user.id, "Чтобы получить информацию о фактической погоде на аэродроме, "
                                                 "введите 4-х буквенную аббревиатуру аэропорта. Если вы хотите узнать аббревиатуру, "
                                                 "или посмотреть список аэропортов, нажмите команду help")


# @dp.message_handler(commands=["history"])
# async def history_command(message: types.Message):
#     pass


@dp.message_handler(content_types="text")
async def get_actual_weather(message: types.Message) -> None:
    response = requests.request(method='GET', url=f'https://api.checkwx.com/metar/{message.text}/decoded',
                                headers={'X-API-Key': API_KEY})
    try:
        data = response.json()
        location = data['data'][0]['station']['location']
        airport = data['data'][0]['station']['name']
        time = data['data'][0]['observed']
        actual_weather = data['data'][0]['raw_text']

        await message.reply(f"*** {datetime.now().strftime('%d-%m-%Y %H:%M')} ***\n"
                            f"City: <b>{location}</b>\nAirport: <b>{airport}</b>\n"
                            f"Release time:\t{time[11:16]}\n"
                            f"<b>{actual_weather}</b>\n")

    except Exception:
        await bot.send_message(message.from_user.id, "Ничего не найдено, попробуйте еще раз.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
