import os
from dotenv import find_dotenv, load_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv(find_dotenv())

TOKEN = os.getenv('TOKEN')
API_KEY = os.getenv('API_KEY')
DEFAULT_COMMANDS = (
        ("start", "Запустить бота"),
        ("help", "Вывести справку"),
        ("description", "Вывести описание бота"),
        ("search", "Вывести список городов"),
        ("history", "Вывести историю запросов"),
        ("close", "Закрыть меню")
    )
