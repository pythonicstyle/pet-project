from loader import dp
from aiogram import types
from keyboards.inline_buttons import help_menu_ikb
from aiogram.dispatcher.filters import Text

HELP = ("🔹 Сайт с подробной расшифровкой метеосводки\n"
        "------------------------------------\n"
        "🔹 Cписок аэропортов и их кодов ИКАО")
HELP_PHOTO = "https://skywaypublic.ru/publications/images/Rasshifrovka_Metar01.jpg"


@dp.message_handler(Text(equals="🆘 help"))
async def help_command(message: types.Message) -> None:
    await message.answer(text=HELP,
                         reply_markup=help_menu_ikb())


@dp.callback_query_handler(Text(equals="photo"))
async def load_photo(callback: types.CallbackQuery) -> None:
    await callback.message.answer_photo(photo=HELP_PHOTO,
                                        caption="Шпаргалка",
                                        reply_markup=help_menu_ikb())
    await callback.message.delete()
