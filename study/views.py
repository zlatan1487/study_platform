from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from study.serliazers import CourseSerializer, LessonSerializer, PaymentSerializer
from study.models import Course, Lesson, Payment
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from django_filters import OrderingFilter
from study.filter.payment_filter import PaymentFilter
from rest_framework.permissions import IsAuthenticated
from study.permissions import BasePermissionMixin, IsOwnerOrModerator # Импортируйте ваш класс разрешений
from rest_framework import viewsets, permissions
from rest_framework.permissions import BasePermission


class CourseViewSet(BasePermissionMixin, viewsets.ModelViewSet):
    """
         Класс CourseViewSet предоставляет CRUD (Create, Retrieve, Update, Delete) операции для модели Course.
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrModerator]  # Разрешение для администраторов (суперпользователей)

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()


class LessonCreateAPIView(BasePermissionMixin, generics.CreateAPIView):
    """
        Класс LessonCreateAPIView предоставляет возможность создания новых уроков.
    """
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]


class LessonListAPIView(generics.ListAPIView):
    """
        Класс LessonListAPIView предоставляет список всех уроков.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrModerator]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """
        Класс LessonRetrieveAPIView предоставляет возможность получения информации о конкретном уроке по его идентификатору.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    """
        Класс LessonUpdateAPIView предоставляет возможность обновления информации о конкретном уроке по его идентификатору.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrModerator]


class LessonDestroyAPIView(BasePermissionMixin, generics.DestroyAPIView):
    """
        Класс LessonDestroyAPIView предоставляет возможность удаления конкретного урока по его идентификатору.
    """
    queryset = Lesson.objects.all()


class LessonCountAPIView(APIView):
    """
        Класс LessonCountAPIView предоставляет информацию о количестве уроков в системе.
    """
    def get(self, request):
        lesson_count = Lesson.objects.count()
        return Response({'lesson_count': lesson_count}, status=status.HTTP_200_OK)


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_class = PaymentFilter

