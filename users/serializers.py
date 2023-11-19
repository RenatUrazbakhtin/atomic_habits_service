from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели пользователя
    """
    def validate_password(self, value:str):
        """
        Метод для хэширования пароля
        """
        return make_password(value)
    class Meta:
        model = User
        fields = '__all__'
