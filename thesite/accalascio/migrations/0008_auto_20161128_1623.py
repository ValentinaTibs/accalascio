# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('accalascio', '0007_auto_20161128_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='catRent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Renting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=80)),
                ('text', tinymce.models.HTMLField()),
                ('active', models.BooleanField(default=False)),
                ('order', models.CharField(max_length=3)),
                ('cat', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='rent', to='accalascio.catRent')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AlterField(
            model_name='iconcat',
            name='png',
            field=models.CharField(max_length=16),
        ),
    ]
