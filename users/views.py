from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from users.models import User
from users.permissions import IsUserOrManager, IsStaff
from users.serializers import UserSerializer


# Create your views here.
class UserCreateAPIView(generics.CreateAPIView):
    """
    Отображение для создания привычки
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    """
    Отображение для удаления привычки
    """
    queryset = User.objects.all()
    permission_classes = [IsUserOrManager]

class UserListAPIView(generics.ListAPIView):
    """
    Отображение для списка привычек
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class UserUpdateAPIView(generics.UpdateAPIView):
    """
    Отображение для обновления привычки
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsUserOrManager]

    def perform_update(self, serializer):
        serializer = serializer.save()
        serializer.save()

class UserRetrieveAPIView(generics.RetrieveAPIView):
    """
    Отображение для получения привычки
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()