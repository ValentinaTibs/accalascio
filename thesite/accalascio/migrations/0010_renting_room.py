# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accalascio', '0009_auto_20161128_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='renting',
            name='room',
            field=models.TextField(blank=True, max_length=80),
        ),
    ]
