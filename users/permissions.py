from rest_framework.permissions import BasePermission


class IsUserOrManager(BasePermission):
    """
    Проверка владельца аккаунта пользователя или админа
    """
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True

        if request.user.pk==view.get_object().pk:
            return True

class IsStaff(BasePermission):
    """
    Проверка является ли пользователь стафом(админом)
    """
    def has_permission(self, request, view):
        return request.user.is_staff