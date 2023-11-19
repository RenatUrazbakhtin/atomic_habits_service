from rest_framework.pagination import PageNumberPagination


class HabitsPagination(PageNumberPagination):
    """
    Пагинация с выводом 5 привычек на страницу
    """
    page_size = 5
    max_page_size = 10