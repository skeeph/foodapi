# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-17 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='publ',
            field=models.BooleanField(default=False),
        ),
    ]