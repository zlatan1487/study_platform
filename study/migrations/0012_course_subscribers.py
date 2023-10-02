# Generated by Django 4.2.5 on 2023-10-01 21:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('study', '0011_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='subscribers',
            field=models.ManyToManyField(related_name='subscribed_courses', to=settings.AUTH_USER_MODEL),
        ),
    ]