from django.db import models
from django.conf import settings
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    preview = models.ImageField(upload_to='course_previews/', verbose_name='Превью', blank=True)
    description = models.TextField(verbose_name='Описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)
    subscribers = models.ManyToManyField(User, related_name='subscribed_courses')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='lesson_previews/', verbose_name='Превью', **NULLABLE)
    video_link = models.URLField(verbose_name='Ссылка на видео', blank=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='lessons', verbose_name='Курс')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Добавляем поле для владельца

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateTimeField()
    paid_course = models.ForeignKey('Course', on_delete=models.CASCADE, **NULLABLE)
    paid_lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, **NULLABLE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method_choices = [
        ('cash', 'Наличные'),
        ('transfer', 'Перевод на счет'),
    ]
    payment_method = models.CharField(max_length=10, choices=payment_method_choices, default='cash')

    def __str__(self):
        return f"{self.user} - {self.payment_date}"


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    subscribed = models.BooleanField(default=False, verbose_name='подписан')

    def __str__(self):
        return f'{self.user} - {self.course} ({self.subscribed})'
