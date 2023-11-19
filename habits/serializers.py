from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from habits.models import Habit
from habits.validators import ValidateTimeToExecute, ValidateRelatedHabitIsPleasant


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор привычки
    """
    time_to_execute = serializers.TimeField(validators=[ValidateTimeToExecute()], required=False)
    related_habit = serializers.PrimaryKeyRelatedField(validators=[ValidateRelatedHabitIsPleasant()], queryset=Habit.objects.all(), required=False)

    class Meta:
        model = Habit
        fields = "__all__"

    def validate(self, attrs):
        "Исключить одновременный выбор связанной привычки и указания вознаграждения."
        if attrs.get('related_habit', False) and attrs.get('reward', False):
            raise ValidationError("Related habit and reward can't be used together in one habit")

        "У приятной привычки не может быть вознаграждения или связанной привычки"
        if attrs.get('is_pleasant', False) is True:
            if attrs.get('reward', False) or attrs.get('related_habit', False):
                raise ValidationError("Pleasant Habit must not have reward or related habit")

        return attrs

