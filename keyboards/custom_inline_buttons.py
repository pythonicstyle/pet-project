from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from handlers.callback_handlers.edit_custom_menu_cb import delete_city_cb


def create_custom_button_ikb(line) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="*** 🌤 METAR ***", callback_data=f"{line[2]}")
            ],
            [
                InlineKeyboardButton(text="❌ Delete city", callback_data=delete_city_cb.new(line[0], "delete"))
            ]
        ]
    )

    return ikb


def custom_menu_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🌆 Add city", callback_data="create_new_menu"),
                InlineKeyboardButton(text="▶️ Open my menu", callback_data="show_custom_menu")
            ]
        ]
    )

    return ikb
