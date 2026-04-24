# Тестовое задание

# Проверяются методы:

- GET /v1/disk/
- PUT /v1/disk/resources (создание папки)
- POST /v1/disk/resources/move (перемещение папки)
- DELETE /v1/disk/resources (удаление папки)

# Запуск через терминал cmd:

1. Создание виртуального окружения:
```
python -m venv .venv
```
3. Активация окружения:
```
.venv\Scripts\Activate
```
3. Установка зависимостей:
```
pip install -r requirements.txt
```
4. Создание файла '.env' с токеном:
```
YADISK_TOKEN=oauth_token
YADISK_BASE_URL=https://cloud-api.yandex.net
```
5. Запуск тестов:
```
python -m pytest
```
