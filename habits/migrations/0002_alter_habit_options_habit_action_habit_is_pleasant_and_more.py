# Generated by Django 4.2.7 on 2023-11-15 15:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habit',
            options={'verbose_name': 'привычка', 'verbose_name_plural': 'привычки'},
        ),
        migrations.AddField(
            model_name='habit',
            name='action',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='действие привычки'),
        ),
        migrations.AddField(
            model_name='habit',
            name='is_pleasant',
            field=models.BooleanField(default=False, verbose_name='признак приятной привычки'),
        ),
        migrations.AddField(
            model_name='habit',
            name='is_public',
            field=models.BooleanField(default=False, verbose_name='признак публикации'),
        ),
        migrations.AddField(
            model_name='habit',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='создатель привычки'),
        ),
        migrations.AddField(
            model_name='habit',
            name='periodicity',
            field=models.CharField(blank=True, choices=[('daily', 'once a day'), ('weekly', 'once a week')], default='daily', max_length=15, null=True, verbose_name='периодичность'),
        ),
        migrations.AddField(
            model_name='habit',
            name='place',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='место для привычки'),
        ),
        migrations.AddField(
            model_name='habit',
            name='related_habit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habits.habit', verbose_name='связанная привычка'),
        ),
        migrations.AddField(
            model_name='habit',
            name='reward',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='вознаграждение'),
        ),
        migrations.AddField(
            model_name='habit',
            name='time',
            field=models.TimeField(blank=True, null=True, verbose_name='время выполнения привычки'),
        ),
        migrations.AddField(
            model_name='habit',
            name='time_to_execute',
            field=models.TimeField(default=datetime.time(0, 2), verbose_name='время на выполнение привычки'),
        ),
    ]
