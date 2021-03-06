# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-02-06 06:38
from __future__ import unicode_literals

import convention.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('convention', '0004_trigger'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(db_index=True, default=convention.models.generate_code, max_length=8, unique=True)),
                ('referred_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referer', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
