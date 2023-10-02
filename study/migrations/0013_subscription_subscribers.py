# Generated by Django 4.2.5 on 2023-10-02 09:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('study', '0012_course_subscribers'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='subscribers',
            field=models.ManyToManyField(blank=True, related_name='subscriptions', to=settings.AUTH_USER_MODEL),
        ),
    ]