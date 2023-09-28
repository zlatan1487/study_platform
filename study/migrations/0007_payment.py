# Generated by Django 4.2.5 on 2023-09-28 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('study', '0006_alter_lesson_video_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(choices=[('cash', 'Наличные'), ('transfer', 'Перевод на счет')], default='cash', max_length=10)),
                ('paid_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='study.course')),
                ('paid_lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='study.lesson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
