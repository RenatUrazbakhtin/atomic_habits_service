import datetime

from rest_framework.exceptions import ValidationError


class ValidateTimeToExecute:
    "Время выполнения должно быть не больше 120 секунд."

    def __call__(self, value):
        if value > datetime.time(0, 2):
            raise ValidationError("Time to execute your habit must be less than 120 seconds")

class ValidateRelatedHabitIsPleasant:
    "В связанные привычки могут попадать только привычки с признаком приятной привычки."

    def __call__(self, value):
        if value.is_pleasant is not True:
            raise ValidationError("Related habit must be pleasant")


