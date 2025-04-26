import os
import sys
from pathlib import Path

from dotenv import load_dotenv

# Определите путь к файлу .env
env_path = Path(__file__).resolve().parent / '.env'

# Загрузка переменных окружения из файла .env
load_dotenv(dotenv_path=env_path)

# Получение переменной окружения
AI_TOKEN = os.getenv("AI_TOKEN")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_ADDR = os.getenv("DB_ADDR")

# Проверка значения переменной
if AI_TOKEN and DB_NAME and DB_USER and DB_PASSWORD and DB_ADDR:
    pass
else:
    sys.exit("Environs from .env does`t load")
