import requests
from celery import shared_task

from config.settings import TELEGRAM_BOT_TOKEN
from habits.models import Habit


@shared_task
def send_habit_tg_task(pk):
    """
    Периодическая отправка привычек через телеграмм бота
    """
    habit = Habit.objects.get(pk=pk)
    chat_id = habit.owner.chat_id
    related_habit = habit.related_habit

    if habit.related_habit:
        text=f'Напоминание о привычке!' '\n' f'{habit.__str__()}' '\n' f'А после {related_habit.__str__}'
    else:
        text=f'Напоминание о привычке!' '\n' f'{habit.__str__()}' '\n' f'И получу {habit.reward}'

    requests.post(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={text}")



