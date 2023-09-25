from study.apps import StudyConfig
from rest_framework.routers import DefaultRouter
from study.views import CourseViewSet

app_name = StudyConfig.name
print('app_name----------', app_name)
router = DefaultRouter()
print("router---------------- ", router)
router.register(r'course', CourseViewSet, basename='course')
urlpatterns = [

] + router.urls
