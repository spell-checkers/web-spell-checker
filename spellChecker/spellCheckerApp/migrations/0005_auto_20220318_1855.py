# Generated by Django 2.2 on 2022-03-18 18:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('spellCheckerApp', '0004_auto_20220318_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='datetime_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 18, 18, 55, 43, 408812, tzinfo=utc)),
        ),
    ]
