# Generated by Django 3.2.6 on 2021-08-13 23:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TelegramBot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='note',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='primo_acquisto',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]