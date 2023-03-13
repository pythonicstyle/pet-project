import requests
from aiogram import types
from keyboards.inline_buttons import moscow_airports_menu_ikb, city_menu__2_ikb, city_menu__3_ikb, city_menu__4_ikb
from keyboards.buttons import main_menu_kb
from loader import dp, bot
from config_data.config import API_KEY
from datetime import datetime


@dp.callback_query_handler()
async def get_actual_weather(callback: types.CallbackQuery) -> None:
    if callback.data == "sub_menu":
        await callback.message.edit_reply_markup(reply_markup=moscow_airports_menu_ikb())
    elif callback.data == "city_menu_2":
        await callback.message.edit_reply_markup(reply_markup=city_menu__2_ikb())
    elif callback.data == "city_menu_3":
        await callback.message.edit_reply_markup(reply_markup=city_menu__3_ikb())
    elif callback.data == "city_menu_4":
        await callback.message.edit_reply_markup(reply_markup=city_menu__4_ikb())
    elif callback.data == "main_menu":
        await bot.send_message(callback.from_user.id,
                               text="Вы вернулись в главное меню",
                               reply_markup=main_menu_kb())
        await callback.message.delete()
    else:
        response = requests.request(method='GET',
                                    url=f'https://api.checkwx.com/metar/{callback.data}/decoded',
                                    headers={'X-API-Key': API_KEY})
        data = response.json()
        location = data['data'][0]['station']['location']
        airport = data['data'][0]['station']['name']
        time = data['data'][0]['observed']
        actual_weather = data['data'][0]['raw_text']

        await bot.send_message(callback.from_user.id, f"*** {datetime.now().strftime('%d-%m-%Y %H:%M')} ***\n"
                                                      f"Город: <b>{location}</b>\nАэропорт: <b>{airport}</b>\n"
                                                      f"Время выпуска сводки:\t{time[11:16]}\n"
                                                      f"<b>{actual_weather}</b>\n")
        await callback.answer()


@dp.message_handler()
async def actual_weather_func(message: types.Message) -> None:
    if len(message.text) == 4:
        response = requests.request(method='GET',
                                    url=f'https://api.checkwx.com/metar/{message.text}/decoded',
                                    headers={'X-API-Key': API_KEY})
        try:
            data = response.json()
            location = data['data'][0]['station']['location']
            airport = data['data'][0]['station']['name']
            time = data['data'][0]['observed']
            actual_weather = data['data'][0]['raw_text']

            await bot.send_message(message.from_user.id, f"*** {datetime.now().strftime('%d-%m-%Y %H:%M')} ***\n"
                                                         f"City: <b>{location}</b>\nAirport: <b>{airport}</b>\n"
                                                         f"Release time:\t{time[11:16]}\n"
                                                         f"<b>{actual_weather}</b>\n")

        except Exception:
            await bot.send_message(message.from_user.id,
                                   text="Ничего не найдено, попробуйте еще раз.")
    else:
        await bot.send_message(message.from_user.id,
                               text="Введите 4-х буквенный код ИКАО или воспользуйтесь меню.")
