# Generated by Django 4.2.5 on 2023-09-25 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0003_course_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='preview',
            field=models.ImageField(blank=True, upload_to='course_previews/', verbose_name='Превью'),
        ),
    ]