# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-03 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accalascio', '0003_auto_20161103_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='icon',
            field=models.TextField(max_length=80, null=True),
        ),
    ]
