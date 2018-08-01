# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-31 10:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('githubApi', '0022_userdetail_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiLogDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='githubApi.UserDetail')),
            ],
        ),
    ]
