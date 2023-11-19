from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from habits.models import Habit
from users.models import User


# Create your tests here.
class HabitTestCase(APITestCase):
    """
    Тесты для модели привычек
    """
    def setUp(self):
        """
        Определение пользователя и привычек для проверки тестов
        """
        self.client = APIClient()

        self.user = User.objects.create(email="testcase@mail.ru", password="testcase", is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=self.user)

        self.pleasant_habit = Habit.objects.create(owner=self.user, place='test1', time="17:00:00", action='test1',
                                                   time_to_execute="00:02:00", is_pleasant=True)
        self.habit = Habit.objects.create(owner=self.user, place='test', time="20:00:00", action='test',
                                          time_to_execute="00:01:00", is_pleasant=False, is_public=True, reward='test')

    def test_create_habit(self):
        data = {
            "time_to_execute": "00:02:00",
            "place": "Нигде",
            "time": '20:00:00',
            "action": "test",
            "is_pleasant": False,
            "periodicity": "1",
            "reward": "Съесть апельсин",
            "is_public": False
        }

        response = self.client.post(
            reverse('habits:habit_create'),
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Habit.objects.all().exists()
        )

    def test_destroy_habit(self):
        response = self.client.delete(
            reverse('habits:habit_destroy', args=[self.pleasant_habit.pk]),
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_list_habit(self):
        response = self.client.get(
            reverse('habits:habit_list')
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_habit(self):
        response = self.client.patch(
            reverse('habits:habit_update', args=[self.habit.pk]),
            data={'reward': 'updated'}
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_retrieve_habit(self):
        response = self.client.get(
            reverse('habits:habit_retrieve', args=[self.habit.pk]),
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_public_habit_list(self):
        response = self.client.get(
            reverse('habits:public_habit_list')
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(response.json(), {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habit.pk,
                    "time_to_execute": self.habit.time_to_execute,
                    "related_habit": self.habit.related_habit,
                    "place": self.habit.place,
                    "time": self.habit.time,
                    "action": self.habit.action,
                    "is_pleasant": self.habit.is_pleasant,
                    "periodicity": self.habit.periodicity,
                    "reward": self.habit.reward,
                    "is_public": self.habit.is_public,
                    "owner": self.habit.owner.pk
                }
            ]
        })
