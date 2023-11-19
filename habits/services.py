from datetime import datetime, timedelta, time


import requests

from django_celery_beat.models import IntervalSchedule, PeriodicTask

from config.settings import TELEGRAM_BOT_TOKEN
from habits.models import Habit
from users.models import User


def get_chat_ids():
    """
    Получение chat_id и nickname пользователей, которые написали боту "привет"
    """
    dict_ids_and_nicknames = {}
    get_updates = requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates")
    json_dict = get_updates.json()
    results = json_dict['result']

    for item in results:
        if item['message']['text'] == 'Привет' or item['message']['text'] == 'привет':
            chat_id = item['message']['chat']['id']
            nickname = item['message']['chat']['username']
            dict_ids_and_nicknames[nickname] = chat_id

    return dict_ids_and_nicknames


def send_welcome_message(chat_id):
    """
    Отправка приветственного сообщения пользователю
    """

    chat_ids = get_chat_ids().values()
    text = "Я буду напоминать вам о вашей привычке, которую вы только что создали"
    if chat_id not in chat_ids:
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={text}")

    # для отладки ниже
    # for chat_id in get_chat_ids().values():
    #     requests.post(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={text}")

def save_user_chat_id(pk):
    """
    Сохранения поля chat_id модели пользователя, который написал боту "привет"
    :param pk:
    :return:
    """
    user = User.objects.get(pk=pk)
    tg_nickname = user.telegram_nickname

    chat_ids = get_chat_ids()

    if tg_nickname in chat_ids.keys():
        chat_id = chat_ids[tg_nickname]
        user.chat_id = chat_id
        user.save()

def create_periodic_task(obj: Habit) -> None:
    """
    Функция, создающая периодическую задачу по данным модели привычки
    """

    schedule, created = IntervalSchedule.objects.get_or_create(
        every=int(obj.periodicity),
        period=IntervalSchedule.DAYS,
    )

    if obj.time:
        if datetime.now().time() < obj.time:
            start_time = datetime.combine(datetime.now().date(), obj.time)
        else:
            start_time = datetime.combine(datetime.today() + timedelta(days=1), obj.time)
    else:
        raise ValueError('Habit must have a time to create a schedule')
    PeriodicTask.objects.create(
        interval=schedule,
        name=obj.pk,
        task='habits.tasks.send_habit_tg_task',
        start_time=start_time,
        args=[obj.pk],
    )
