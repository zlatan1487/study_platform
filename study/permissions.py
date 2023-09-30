from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import BasePermission


class BasePermissionMixin(BasePermission):
    """
    Базовый класс для представлений, предоставляющий общую логику проверки разрешений.
    """
    def create(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return Response({'detail': 'Модераторы не могут создавать объекты'}, status=status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return Response({'detail': 'Модераторы не могут удалять объекты'}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)


class IsOwnerOrModerator(BasePermission):
    """
    Пользователи могут редактировать курсы только если они являются владельцем курса
    или модераторами.
    """
    message = "Вы не являетесь владельцем или модератором данного курса."

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        return obj.owner == request.user



