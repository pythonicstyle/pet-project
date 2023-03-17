import logging
import requests
from aiogram import types
from datetime import datetime

from loader import dp, bot
from config_data.config import API_KEY
from keyboards.buttons import main_menu_kb
from keyboards.inline_buttons import moscow_airports_menu_ikb, city_menu_ikb, \
    city_menu__2_ikb, city_menu__3_ikb, city_menu__4_ikb

logging.basicConfig(level=logging.ERROR)


@dp.callback_query_handler()
async def get_actual_weather(callback: types.CallbackQuery) -> None:
    """
    Функция обрабатывает любой callback запрос,
    который не был обработан другими хэндлерами
    и выводит пользователю следующее меню
    либо информацию о погоде на выбранном аэропорту
    """
    if callback.data == "sub_menu":
        await callback.message.edit_reply_markup(reply_markup=moscow_airports_menu_ikb())
    elif callback.data == "city_menu":
        await callback.message.edit_reply_markup(reply_markup=city_menu_ikb())
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
        try:
            response = requests.request(method='GET',
                                        url=f'https://api.checkwx.com/metar/{callback.data}/decoded',
                                        headers={'X-API-Key': API_KEY})
            data = response.json()
            location = data['data'][0]['station']['location']
            airport = data['data'][0]['station']['name']
            time = data['data'][0]['observed']
            actual_weather = data['data'][0]['raw_text']

            await callback.message.answer(f"*** {datetime.now().strftime('%d-%m-%Y %H:%M')} ***\n"
                                          f"Город: <b>{location}</b>\nАэропорт: <b>{airport}</b>\n"
                                          f"Время выпуска сводки:\t{time[11:16]}\n"
                                          f"<b>{actual_weather}</b>\n")
            await callback.answer()
        except Exception:
            await callback.message.answer(f"🗿 По запросу '{callback.data}' ничего не найдено."
                                          f"Возможно, на сайте просто нет информации о таком аэропорте 🗿")
            logging.error(f"user_id={callback.from_user.id} user={callback.from_user.full_name} - request={callback.data}")
            await callback.answer()


@dp.message_handler()
async def actual_weather_func(message: types.Message) -> None:
    """
    Функция обрабатывает любое сообщение пользователя,
    которое не было обработано другими хэндлерами и
    выводит пользователю информацию о погоде
    либо сообщение об ошибке.
    """
    if len(message.text) == 4 and message.text.isalpha():
        response = requests.request(method='GET',
                                    url=f'https://api.checkwx.com/metar/{message.text}/decoded',
                                    headers={'X-API-Key': API_KEY})
        try:
            data = response.json()
            location = data['data'][0]['station']['location']
            airport = data['data'][0]['station']['name']
            time = data['data'][0]['observed']
            actual_weather = data['data'][0]['raw_text']

            await message.answer(f"*** {datetime.now().strftime('%d-%m-%Y %H:%M')} ***\n"
                                 f"Город: <b>{location}</b>\nАэропорт: <b>{airport}</b>\n"
                                 f"Время выпуска сводки:\t{time[11:16]}\n"
                                 f"<b>{actual_weather}</b>\n")

        except Exception:
            await message.answer("Ничего не найдено, попробуйте еще раз.")
            logging.error(f"user_id={message.from_user.id} user={message.from_user.full_name} - request={message.text}")
    else:
        await message.answer("Это не похоже на аббревиатуру кода 🤔\n"
                             "Введите 4-х буквенный код ИКАО или воспользуйтесь меню.")
