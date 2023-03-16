from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main_menu_kb() -> ReplyKeyboardMarkup:
    main_menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🔎 search"),
                KeyboardButton(text="🆘 help")
            ],
            [
                KeyboardButton(text="📎 description"),
                KeyboardButton(text="⚙️ custom menu")
            ],
            [
                KeyboardButton(text="✖️ close keyboard")
            ]
        ], resize_keyboard=True, one_time_keyboard=True
    )

    return main_menu


def cancel_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📌 main menu")
            ]
        ], resize_keyboard=True
    )

    return kb
