from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main_menu_kb() -> ReplyKeyboardMarkup:
    main_menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="/search"),
                KeyboardButton(text="/help")
            ],
            [
                KeyboardButton(text="/description"),
                KeyboardButton(text="/history")
            ],
            [
                KeyboardButton(text="/close")
            ]
        ], resize_keyboard=True, one_time_keyboard=True
    )

    return main_menu
