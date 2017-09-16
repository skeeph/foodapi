from django.db import models
from django.contrib.postgres.fields import ArrayField

from users.models import User


class Week(models.Model):
    num = models.IntegerField()
    user = models.ForeignKey(User, related_name='weeks')
    mon = ArrayField(models.CharField(max_length=64))
    tue = ArrayField(models.CharField(max_length=64))
    wed = ArrayField(models.CharField(max_length=64))
    thu = ArrayField(models.CharField(max_length=64))
    fri = ArrayField(models.CharField(max_length=64))
    sat = ArrayField(models.CharField(max_length=64))
    sun = ArrayField(models.CharField(max_length=64))
