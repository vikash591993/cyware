# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-30 13:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('githubApi', '0016_userdetail_avatar_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='avatar_url',
        ),
    ]