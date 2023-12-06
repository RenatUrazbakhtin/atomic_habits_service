# atomic_habits_service

## Описание проекта
Сервис управления полезными привычками и получения напоминаний о необходимости их выполнения в виде сообщений через Telegram

В рамках проекта реализованна backend часть SPA веб приложения

## Технологии
- Python
- Pip
- Django
- DRF
- PostgreSQL
- Redis
- Celery
- Docker
- Docker-compose

## Зависимости
Зависимости проекта находятся в файле requirements

Установить зависимости можно с помощью команды pip install -r requirements

## env_sample
POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT - данные для подключения к бд

TELEGRAM_BOT_TOKEN - api ключ телеграм

SECRET_KEY - ключ django

## Работа с проектом
Для запуска проекта необходимо выполнить следующие шаги:
1) Установить на компьютер Docker и Docker Compose с помощью инструкции [https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/)
2) Клонировать репозиторий себе на компьютер
3) Создать файл .env по примеру .env_sample
4) Собрать Docker образ с помощью команды `docker-compose build`
5) Запустить контейнер с помощью команды `docker-compose up`
6) Создайте телеграм-бота используя телеграм-бот @BotFather и получите от него API ключ 
7) Пройдите регистрацию, авторизацию сервиса
8) Напишите боту приветсвенное сообщение `Привет`
9) Создайте привычку

Далее автоматически будет создана периодическая задача Celery которая будет высылать созданную привычку с выбранной периодичностью и временем.

## Документация по ссылкам
Swagger - `swagger/`

Redoc - `redoc/`

