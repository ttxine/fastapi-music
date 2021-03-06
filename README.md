# FastAPI Music

## Описание
REST API музыкального сервиса на FastAPI
### Стек технологий
- Python 3.10
- FastAPI
- SQLite
# Начало работы
1) Виртуальное окружение
    ```
    python -m venv venv
    ```
2) Установить зависимости
    ```
    pip install -r requirements.txt
    ```
3) Создать `.env` файл и установить переменные окружения. Пример из `.env.example`:
    ```
    SITE_DOMAIN=...
    DATABASE_URL=...
    ACCESS_TOKEN_TYPE=...
    ACCESS_TOKEN_SECRET_KEY=...
    REFRESH_TOKEN_TYPE=...
    REFRESH_TOKEN_SECRET_KEY=...
    EMAIL_CONFIRMATION_TOKEN_TYPE=...
    EMAIL_CONFIRMATION_TOKEN_SECRET_KEY=...
    PASSWORD_RESET_TOKEN_TYPE=..
    PASSWORD_RESET_TOKEN_SECRET_KEY=...
    MAIL_USERNAME=...
    MAIL_PASSWORD=...
    MAIL_FROM=...
    MAIL_PORT=...
    MAIL_SERVER=...
    ```
4) Выполнить миграции
    ```
    alembic upgrade head
    ```
5) Создать суперпользователя
    ```
    python main.py createsuperuser
    ```
6) Запуск сервера
    ```
    python main.py runserver --reload
    ```
