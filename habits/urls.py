from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitDestroyAPIView, HabitListAPIView, HabitUpdateAPIView, \
    HabitRetrieveAPIView, PublicHabitListAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habit/destroy/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_destroy'),
    path('habit/list/', HabitListAPIView.as_view(), name='habit_list'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habit/retrieve/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_retrieve'),
    path('habit/public/list/', PublicHabitListAPIView.as_view(), name='public_habit_list')
]