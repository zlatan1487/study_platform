from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from study.serliazers import CourseSerializer, LessonSerializer, PaymentSerializer, SubscriptionSerializer
from study.models import Course, Lesson, Payment, Subscription
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import OrderingFilter, rest_framework as filters
from study.filter.payment_filter import PaymentFilter
from rest_framework.permissions import IsAuthenticated
from study.permissions import BasePermissionMixin, IsOwnerOrModerator
from rest_framework import viewsets, permissions
from rest_framework.permissions import BasePermission
from rest_framework.decorators import action


class CourseViewSet(BasePermissionMixin, viewsets.ModelViewSet):
    """
         Класс CourseViewSet предоставляет CRUD (Create, Retrieve, Update, Delete) операции для модели Course.
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        # Инвертируем логику: is_subscribed будет True для подписанных и False для не подписанных
        subscribed = instance.subscribers.filter(id=request.user.id).exists()
        data = serializer.data
        data['is_subscribed'] = subscribed
        return Response(data)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def perform_create(self, serializer):
        new_course = serializer.save(owner=self.request.user)
        new_course.is_subscribed = False
        new_course.save()


    @action(detail=True, methods=['post'])
    def subscribe(self, request, pk=None):
        course = self.get_object()
        user = request.user

        # Проверка, что пользователь еще не подписан на этот курс
        try:
            subscription = Subscription.objects.get(user=user, course=course)
            subscription.subscribed = True
            subscription.save()
        except Subscription.DoesNotExist:
            Subscription.objects.create(user=user, course=course, subscribed=True)

        # Добавляем пользователя в поле subscribers у курса
        course.subscribers.add(user)
        course.save()

        return Response({'status': 'Subscribed'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def unsubscribe(self, request, pk=None):
        course = self.get_object()
        user = request.user

        # Проверка, что пользователь подписан на этот курс
        try:
            subscription = Subscription.objects.get(user=user, course=course)
            subscription.subscribed = False
            subscription.save()
        except Subscription.DoesNotExist:
            return Response({'error': 'Not subscribed to this course'}, status=status.HTTP_400_BAD_REQUEST)

        # Удаляем пользователя из поля subscribers у курса
        course.subscribers.remove(user)
        course.save()

        return Response({'status': 'Unsubscribed'}, status=status.HTTP_200_OK)




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
        Класс LessonCountAPIView предоставляет информацию о количестве уроков в курсе
    """
    def get(self, request):
        lesson_count = Lesson.objects.count()
        return Response({'lesson_count': lesson_count}, status=status.HTTP_200_OK)


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_class = PaymentFilter
