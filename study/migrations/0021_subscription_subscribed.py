# Generated by Django 4.2.5 on 2023-10-02 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0020_alter_subscription_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='subscribed',
            field=models.BooleanField(default=False, verbose_name='подписан'),
        ),
    ]
