import datetime

import django.utils.timezone as timezone
from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=20)
    email = models.CharField(default="", max_length=255)
    datetime_created = models.DateTimeField(timezone.now())

    def __str__(self):
        return self.username

    def is_new(self):
        return self.datetime_created >= timezone.now() - datetime.timedelta(days=1)
