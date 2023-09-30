from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}

class User(AbstractUser):
    pass

# class UserManager(BaseUserManager):
#     def create_user(self, email, phone, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, phone=phone, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, phone, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#
#         return self.create_user(email, phone, password, **extra_fields)
#
#
# class User(AbstractUser, PermissionsMixin):
#     date_joined = models.DateTimeField(default=timezone.now)
#     email = models.EmailField(unique=True, verbose_name='почта', **NULLABLE)
#     phone = models.CharField(max_length=15, verbose_name='телефон', **NULLABLE)
#     first_name = models.CharField(max_length=30, verbose_name='имя', **NULLABLE)
#     last_name = models.CharField(max_length=30, verbose_name='фамилия', **NULLABLE)
#     city = models.CharField(max_length=100, verbose_name='город', **NULLABLE)
#     avatar = models.ImageField(upload_to='avatars/', verbose_name='аватар', **NULLABLE)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['phone']
#
#     def get_by_natural_key(self):
#         return self.email
#
#     def __str__(self):
#         return self.email
#
#

