# Generated by Django 2.2 on 2022-03-18 18:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('spellCheckerApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='userid',
        ),
        migrations.AddField(
            model_name='user',
            name='datetime_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 18, 18, 47, 14, 454265, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='', max_length=255),
        ),
    ]
