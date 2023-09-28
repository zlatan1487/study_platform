from django.core.management.base import BaseCommand
from django.utils import timezone
from study.models import Payment, Course, Lesson
from users.models import User


class Command(BaseCommand):
    help = 'Create sample payments'

    def handle(self, *args, **kwargs):
        # Получите существующих пользователей, курсы и уроки
        user1 = User.objects.get(email='user@example.com')  # Замените на реальные значения
        course1 = Course.objects.get(title='Курс французского языка', description='приходите на уроки французского языка, вам очень понравиться')
        lesson1 = Lesson.objects.get(id=7)  # Замените на реальные значения

        user2 = User.objects.get(email='user1@example.com')  # Замените на реальные значения
        course2 = Course.objects.get(title='Курс програмирования на python', description='Приглашаем на курс по python и django')
        lesson2 = Lesson.objects.get(id=8)  # Замените на реальные значения

        user3 = User.objects.get(email='user2@example.com')  # Замените на реальные значения
        course3 = Course.objects.get(title='Курс молодого бойца', description='Приглашаем на курс молодого бойца, для тех кто хочет стать настоящим мужчиной')
        lesson3 = Lesson.objects.get(id=9)  # Замените на реальные значения

        user4 = User.objects.get(email='user@example.com')  # Замените на реальные значения
        course4 = Course.objects.get(title='Курс французского языка',
                                     description='приходите на уроки французского языка, вам очень понравиться')
        lesson4 = Lesson.objects.get(id=10)  # Замените на реальные значения

        user5 = User.objects.get(email='user1@example.com')  # Замените на реальные значения
        course5 = Course.objects.get(title='Курс програмирования на python',
                                     description='Приглашаем на курс по python и django')
        lesson5 = Lesson.objects.get(id=11)  # Замените на реальные значения

        user6 = User.objects.get(email='user2@example.com')  # Замените на реальные значения
        course6 = Course.objects.get(title='Курс молодого бойца',
                                     description='Приглашаем на курс молодого бойца, для тех кто хочет стать настоящим мужчиной')
        lesson6 = Lesson.objects.get(id=12)  # Замените на реальные значения

        Payment.objects.create(
            user=user1,
            payment_date=timezone.now(),
            paid_course=course1,
            paid_lesson=lesson1,
            amount=50.00,
            payment_method='cash'
        )

        Payment.objects.create(
            user=user3,
            payment_date=timezone.now(),
            paid_course=course3,
            paid_lesson=lesson3,
            amount=70.00,
            payment_method='transfer'
        )

        Payment.objects.create(
            user=user2,
            payment_date=timezone.now(),
            paid_course=course2,
            paid_lesson=lesson2,
            amount=90.00,
            payment_method='transfer'
        )

        Payment.objects.create(
            user=user4,
            payment_date=timezone.now(),
            paid_course=course4,
            paid_lesson=lesson4,
            amount=150.00,
            payment_method='cash'
        )

        Payment.objects.create(
            user=user5,
            payment_date=timezone.now(),
            paid_course=course5,
            paid_lesson=lesson5,
            amount=170.00,
            payment_method='transfer'
        )

        Payment.objects.create(
            user=user6,
            payment_date=timezone.now(),
            paid_course=course6,
            paid_lesson=lesson6,
            amount=190.00,
            payment_method='cash'
        )

        self.stdout.write(self.style.SUCCESS('Successfully created payments'))
