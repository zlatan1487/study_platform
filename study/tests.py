
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User  # Импортируйте модель пользователя, если она не была импортирована ранее
from study.models import Course, Subscription  # Импортируйте модель Course, если она не была импортирована ранее
from rest_framework_simplejwt.tokens import RefreshToken


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        # Создайте пользователя и получите JWT-токен
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_lesson(self):
        """
        Test lesson creation.
        """

        url = reverse('study:lesson_create')
        new_course = Course.objects.create(title='New Course', description='Course Description')

        data = {
            'title': 'New Course',
            'description': 'Course Description',
            "video_link": "https://www.youtube.com/watch?v=LTg4BfCskHw",
            "course": new_course.id
        }

        response = self.client.post(url, data, format='json')
        if response.status_code != status.HTTP_201_CREATED:
            print(response.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Course.objects.filter(title='New Course').exists())


class SubscribeTestCase(APITestCase):

    def setUp(self) -> None:
        # Создайте пользователя и получите JWT-токен
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_subscribe_to_course(self):
        course = Course.objects.create(
            title='Курс на который подпишусь',
            description='Курс на который подпишусь - Python',
        )

        url = reverse('study:course-subscribe', kwargs={'pk': course.pk})

        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'Subscribed')

        subscription = Subscription.objects.get(user=self.user, course=course)
        self.assertTrue(subscription.subscribed)

    def test_unsubscribe_from_course(self):
        course = Course.objects.create(title='Курс от которого отпишусь', description='Курс от которого отписался')
        subscription = Subscription.objects.create(user=self.user, course=course, subscribed=True)

        url = reverse('study:course-unsubscribe', kwargs={'pk': course.pk})

        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'Unsubscribed')

        subscription.refresh_from_db()
        self.assertFalse(subscription.subscribed)
