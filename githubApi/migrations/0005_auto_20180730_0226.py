# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-29 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('githubApi', '0004_auto_20180730_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='image',
            field=models.CharField(default=0, max_length=1000000),
        ),
    ]
