# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-12 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mete', '0005_auto_20160503_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_disabled',
            field=models.BooleanField(default=False),
        ),
    ]
