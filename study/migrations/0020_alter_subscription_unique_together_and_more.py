# Generated by Django 4.2.5 on 2023-10-02 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('study', '0019_subscription_subscribed_alter_subscription_course_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.course', verbose_name='курс'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='subscribed',
        ),
    ]
