# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 12:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mete', '0003_log_product_purchase'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='locked',
            new_name='is_locked',
        ),
        migrations.RemoveField(
            model_name='account',
            name='disabled',
        ),
    ]
