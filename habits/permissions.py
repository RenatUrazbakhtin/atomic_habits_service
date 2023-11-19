from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Проверка является ли пользователь владельцем привычки
    """
    def has_permission(self, request, view):
        return request.user==view.get_object().owner