# Generated by Django 4.2.5 on 2023-09-28 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0007_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='lesson_previews/', verbose_name='Превью'),
        ),
    ]