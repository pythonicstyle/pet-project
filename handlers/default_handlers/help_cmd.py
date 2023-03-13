from loader import dp
from aiogram import types
from keyboards.inline_buttons import help_menu_ikb

HELP = ("- Сайт с подробной расшифровкой метеосводки\n"
        "- Cписок аэропортов и их кодов ИКАО")
HELP_PHOTO = "https://skywaypublic.ru/publications/images/Rasshifrovka_Metar01.jpg"


@dp.message_handler(commands=["help"])
async def help_command(message: types.Message) -> None:
    await message.answer_photo(photo=HELP_PHOTO,
                               caption="Шпаргалка")
    await message.answer(text=HELP,
                         reply_markup=help_menu_ikb())
