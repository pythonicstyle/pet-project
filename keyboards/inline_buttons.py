from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


help_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Таблица расшифровки", url="https://skywaypublic.ru/publ/meteorologija/rasshifrovka_meteokoda_metar_shpargalka/6-1-0-40"),
            InlineKeyboardButton(text="Список аэропортов", url="http://www.flugzeuginfo.net/table_airportcodes_country-location_en.php")
        ]
    ]
)