

from django.db import models

from config import settings

NULLABLE = {'null': True, 'blank': True}
# Create your models here.
class Habit(models.Model):
    """
    Модель привычки
    """
    CHOICES = (
        ('1', 'Раз в день'),
        ('2', 'Раз в два дня'),
        ('3', 'Раз в три дня'),
        ('4', 'Раз в четыре дня'),
        ('5', 'Раз в пять дней'),
        ('6', 'Раз в шесть дней'),
        ('7', 'Раз в неделю'),
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="создатель привычки", **NULLABLE)
    place = models.CharField(max_length=255, verbose_name="место для привычки", **NULLABLE)
    time = models.TimeField(verbose_name="время выполнения привычки", **NULLABLE)
    action = models.CharField(max_length=255, verbose_name="действие привычки", **NULLABLE)
    is_pleasant = models.BooleanField(default=False, verbose_name="признак приятной привычки")
    related_habit = models.ForeignKey('Habit', on_delete=models.CASCADE, verbose_name="связанная привычка", **NULLABLE)
    periodicity = models.CharField(max_length=15, choices=CHOICES, default='1', verbose_name='периодичность', **NULLABLE)
    reward = models.CharField(max_length=100, verbose_name="вознаграждение", **NULLABLE)
    time_to_execute = models.TimeField(verbose_name="время на выполнение привычки")
    is_public = models.BooleanField(default=False, verbose_name="признак публикации")

    def __str__(self):
        return f'Я буду {self.action} в {self.place} в {self.time} и получу {self.reward}'

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"