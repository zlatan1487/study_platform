from django.urls import path
from study.apps import StudyConfig
from rest_framework.routers import DefaultRouter
from study.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, LessonDestroyAPIView, LessonCountAPIView, PaymentListAPIView

app_name = StudyConfig.name

router = DefaultRouter()

router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
    path('lesson/number_of_lessons/', LessonCountAPIView.as_view(), name='lesson-count'),
    path('payment/', PaymentListAPIView.as_view(), name='payment-list'),
    path('course/<int:pk>/subscribe/', CourseViewSet.as_view({'post': 'subscribe'}), name='course-subscribe'),
    path('course/<int:pk>/unsubscribe/', CourseViewSet.as_view({'delete': 'unsubscribe'}), name='course-unsubscribe'),
] + router.urls
