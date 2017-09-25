from __future__ import unicode_literals

import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible
# noinspection PyUnresolvedReferences
from recipes.models import Recipe

# from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def get_recipes(self):
        return (self.recipes.all() | Recipe.objects.filter(publ=True)).distinct()

    def __str__(self):
        return self.username


class Settings(models.Model):
    user = models.OneToOneField(User, related_name="settings")
    apikey = models.CharField(max_length=64)
    project_name = models.CharField(max_length=120)
