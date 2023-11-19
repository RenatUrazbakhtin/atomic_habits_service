from django.shortcuts import render
from rest_framework import generics


from habits.models import Habit
from habits.paginators import HabitsPagination
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer
from habits.services import send_welcome_message, save_user_chat_id, create_periodic_task



# Create your views here.
class HabitCreateAPIView(generics.CreateAPIView):
    """
    Отображение для создания привычки
    """
    serializer_class = HabitSerializer
    def perform_create(self, serializer):
        """
        переопределение полей владельца привычки и основной скрипт рассылки
        """
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()
        save_user_chat_id(new_habit.owner.pk)
        send_welcome_message(new_habit.owner.chat_id)
        if not new_habit.is_pleasant:
            create_periodic_task(new_habit)

class HabitDestroyAPIView(generics.DestroyAPIView):
    """
    Отображение для удаления привычки
    """
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]

class HabitUpdateAPIView(generics.UpdateAPIView):
    """
    Отображение для обновления привычки
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]

    def perform_update(self,serializer):
        """
        Метод для сохранения изменений привычки
        :param serializer:
        :return:
        """
        updated_habit = serializer.save()
        updated_habit.save()

class HabitListAPIView(generics.ListAPIView):
    """
    Отображение для списка привычек
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitsPagination

    def get_queryset(self):
        """
        Метод который показывает пользователю только его привычки
        """
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset

class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """
    Отображение для получения привычки
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

class PublicHabitListAPIView(generics.ListAPIView):
    """
    Отображение для списка публичных привычек
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitsPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_public=True)

        return queryset