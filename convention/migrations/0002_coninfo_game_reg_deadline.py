# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-09 03:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('convention', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coninfo',
            name='game_reg_deadline',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 16, 1, 0, tzinfo=utc)),
        ),
    ]