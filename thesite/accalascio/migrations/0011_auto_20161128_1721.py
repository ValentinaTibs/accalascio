# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 17:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accalascio', '0010_renting_room'),
    ]

    operations = [
        migrations.RenameField(
            model_name='renting',
            old_name='room',
            new_name='png',
        ),
    ]
