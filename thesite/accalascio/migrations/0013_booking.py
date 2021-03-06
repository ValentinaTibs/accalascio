# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-19 16:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accalascio', '0012_auto_20161128_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('notes', models.TextField(max_length=180, null=True)),
                ('contacts_mail', models.EmailField(max_length=254)),
                ('checkin_time', models.TimeField(null=True)),
                ('room', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='accalascio.Renting')),
            ],
        ),
    ]
