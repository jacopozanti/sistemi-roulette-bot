# Generated by Django 3.2.6 on 2021-08-13 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TelegramBot', '0002_auto_20210813_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='primo_acquisto',
        ),
    ]
