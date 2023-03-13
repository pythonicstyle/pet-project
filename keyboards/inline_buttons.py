from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

users_cb = CallbackData('user', 'id', 'action')


def help_menu_ikb() -> InlineKeyboardMarkup:
    help_menu = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="METAR decoding",
                                     url="https://skywaypublic.ru/publ/meteorologija/rasshifrovka_meteokoda_metar_shpargalka/6-1-0-40"),
                InlineKeyboardButton(text="ICAO Airports",
                                     url="http://www.flugzeuginfo.net/table_airportcodes_country-location_en.php")
            ],
            [
                InlineKeyboardButton(text="📌 Главное меню", callback_data="main_menu")
            ]
        ]
    )
    return help_menu


def city_menu_ikb() -> InlineKeyboardMarkup:
    city_menu = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Москва", callback_data='sub_menu'),
                InlineKeyboardButton(text="Санкт-Петербург", callback_data="ULLI"),
                InlineKeyboardButton(text="Казань", callback_data="UWKD")
            ],
            [
                InlineKeyboardButton(text="Екатеринбург", callback_data="USSS"),
                InlineKeyboardButton(text="Сочи", callback_data="URSS"),
                InlineKeyboardButton(text="Нижний Новгород", callback_data="UWGG")
            ],
            [
                InlineKeyboardButton(text="Калининград", callback_data="UMKK"),
                InlineKeyboardButton(text="Хабаровск", callback_data="UHHH"),
                InlineKeyboardButton(text="Иркутск", callback_data="UIII ")
            ],
            [
                InlineKeyboardButton(text="📌 Главное меню", callback_data="main_menu"),
                InlineKeyboardButton(text="Следующая страница ➡️", callback_data="city_menu_2")
            ]
        ]
    )

    return city_menu


def city_menu__2_ikb() -> InlineKeyboardMarkup:
    city_menu_2 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Архангельск", callback_data="ULAA"),
                InlineKeyboardButton(text="Анадырь", callback_data="UHMA"),
                InlineKeyboardButton(text="Анапа", callback_data="URKA"),
            ],
            [
                InlineKeyboardButton(text="Благовещенск", callback_data="UHBB"),
                InlineKeyboardButton(text="Бегишево", callback_data="UWKE"),
                InlineKeyboardButton(text="Владивосток", callback_data="UHWW")
            ],
            [
                InlineKeyboardButton(text="Владикавказ", callback_data="URMO"),
                InlineKeyboardButton(text="Грозный", callback_data="URMG"),
                InlineKeyboardButton(text="Краснодар", callback_data="URKK"),
            ],
            [
                InlineKeyboardButton(text="⬅️ Предыдущая страница", callback_data="main_menu"),
                InlineKeyboardButton(text="Следующая страница ➡️", callback_data="city_menu_3")
            ]
        ]
    )

    return city_menu_2


def city_menu__3_ikb() -> InlineKeyboardMarkup:
    city_menu_3 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Красноярск", callback_data="UNKL"),
                InlineKeyboardButton(text="Липецк", callback_data="UUOL"),
                InlineKeyboardButton(text="Магадан", callback_data="UHMM")
            ],
            [
                InlineKeyboardButton(text="Магнитогорск", callback_data="USCM"),
                InlineKeyboardButton(text="Минеральные Воды", callback_data="URMM"),
                InlineKeyboardButton(text="Норильск", callback_data="UOOO")
            ],
            [
                InlineKeyboardButton(text="Оренбург", callback_data="UWOO "),
                InlineKeyboardButton(text="Орск", callback_data="UWOR"),
                InlineKeyboardButton(text="Пермь", callback_data="USPP")

            ],
            [
                InlineKeyboardButton(text="⬅️ Предыдущая страница", callback_data="city_menu_2"),
                InlineKeyboardButton(text="Следующая страница ➡️", callback_data="city_menu_4")
            ]
        ]
    )

    return city_menu_3


def city_menu__4_ikb() -> InlineKeyboardMarkup:
    city_menu_4 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Псков", callback_data="ULOO"),
                InlineKeyboardButton(text="Тюмень", callback_data="USTR"),
                InlineKeyboardButton(text="Ульяновск", callback_data="UWLL")
            ],
            [
                InlineKeyboardButton(text="Уфа", callback_data="UWUU"),
                InlineKeyboardButton(text="Ханты-Мансийск", callback_data="USHH"),
                InlineKeyboardButton(text="Самара", callback_data="UWWW")
            ],
            [
                InlineKeyboardButton(text="Чебоксары", callback_data="UWKS"),
                InlineKeyboardButton(text="Челябинск", callback_data="USCC"),
                InlineKeyboardButton(text="Якутск", callback_data="UEEE")
            ],
            [
                InlineKeyboardButton(text="⬅️ Предыдущая страница", callback_data="city_menu_3")
            ]
        ]
    )

    return city_menu_4


def moscow_airports_menu_ikb() -> InlineKeyboardMarkup:
    moscow_airports_menu = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Шереметьево", callback_data="UUEE"),
                InlineKeyboardButton(text="Домодедово", callback_data="UUDD")
            ],
            [
                InlineKeyboardButton(text="Внуково", callback_data="UUWW"),
                InlineKeyboardButton(text="Жуковский", callback_data="UUBW ")
            ],
            [
                InlineKeyboardButton(text="📌 Главное меню", callback_data="main_menu"),
            ]
        ]
    )

    return moscow_airports_menu
