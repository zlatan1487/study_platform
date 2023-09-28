from django.shortcuts import render
from rest_framework import viewsets, generics
from study.serliazers import CourseSerializer, LessonSerializer
from study.models import Course, Lesson
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class CourseViewSet(viewsets.ModelViewSet):
    """
         Класс CourseViewSet предоставляет CRUD (Create, Retrieve, Update, Delete) операции для модели Course.
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    """
        Класс LessonCreateAPIView предоставляет возможность создания новых уроков.
    """
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    """
        Класс LessonListAPIView предоставляет список всех уроков.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


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


class LessonDestroyAPIView(generics.DestroyAPIView):
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
