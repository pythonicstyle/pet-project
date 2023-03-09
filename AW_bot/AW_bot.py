import requests
from datetime import datetime
from aiogram import types
from aiogram.utils import executor

from main import dp, bot
from config import API_KEY
from keyboards.user_buttons import menu, sub_menu, other_menu


@dp.message_handler(commands=["start"])
async def start_menu(message: types.Message):
    greeting = f"<b>Привет, {message.from_user.first_name}!</b>"
    await bot.send_message(message.chat.id, greeting)
    await message.answer(text="Выберете дальнейшее действие из меню или введите 4-х буквенный код аэропорта")


@dp.message_handler(commands=["help"])
async def load_photo(message: types.Message):
    await bot.send_message(message.chat.id, "Для удобства расшифровки, можно воспользоваться табличкой :)")
    photo = open('img.png', 'rb')
    await bot.send_photo(message.chat.id, photo)


@dp.message_handler(content_types='text')
async def get_actual_weather(message: types.Message):
    response = requests.request(method='GET', url=f'https://api.checkwx.com/metar/{message.text}/decoded',
                                headers={'X-API-Key': API_KEY})
    if response.status_code == 200:
        try:
            data = response.json()
            location = data['data'][0]['station']['location']
            airport = data['data'][0]['station']['name']
            time = data['data'][0]['observed']
            actual_weather = data['data'][0]['raw_text']

            await message.answer(f"*** {datetime.now().strftime('%d-%m-%Y %H:%M')} ***\n"
                                 f"City: {location}\nAirport: {airport}\n"
                                 f"Release time: {time}\n"
                                 f"{actual_weather}\n")

        except Exception as exc:
            await bot.send_message(message.from_user.id, "Error:", exc)
    else:
        await bot.send_message(message.from_user.id, "didn't found :(")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
