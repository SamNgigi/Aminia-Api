# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-14 14:18
from __future__ import unicode_literals

from django.db import migrations, models
import post_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=75, validators=[post_app.validators.validate_content]),
        ),
    ]
