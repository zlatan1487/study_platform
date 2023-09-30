from django.core.management.base import BaseCommand
from django.utils import timezone
from study.models import Payment, Course, Lesson
from users.models import User


class Command(BaseCommand):
    help = 'Create sample payments'

    def handle(self, *args, **kwargs):
        # Получите существующих пользователей, курсы и уроки
        user1 = User.objects.get(id=1)  # Замените на реальные значения
        course1 = Course.objects.get(title='Курс французского языка', description='приходите на уроки французского языка, вам очень понравиться')
        lesson1 = Lesson.objects.get(id=3)  # Замените на реальные значения

        user2 = User.objects.get(id=2)  # Замените на реальные значения
        course2 = Course.objects.get(title='Курс програмирования на python', description='Приглашаем на курс по python и django')
        lesson2 = Lesson.objects.get(id=2)  # Замените на реальные значения

        user3 = User.objects.get(id=3)  # Замените на реальные значения
        course3 = Course.objects.get(title='Курс молодого бойца', description='Приглашаем на курс молодого бойца, для тех кто хочет стать настоящим мужчиной')
        lesson3 = Lesson.objects.get(id=1)  # Замените на реальные значения

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

        self.stdout.write(self.style.SUCCESS('Successfully created payments'))
