import os

from dotenv import load_dotenv

load_dotenv()

# Базовый адрес API Яндекс.Диска
BASE_URL = os.getenv("YADISK_BASE_URL", "https://cloud-api.yandex.net").rstrip("/")

# Токен берём из .env
TOKEN = os.getenv("YADISK_TOKEN", "")

# Префикс для тестовых папок
TEST_DIR_PREFIX = "test_autotest"
