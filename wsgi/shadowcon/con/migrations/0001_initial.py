# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 04:31
from __future__ import unicode_literals

import ckeditor.fields
import con.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.CharField(choices=[('M', 'Maybe'), ('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='ConInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('pre_reg_deadline', models.DateField()),
                ('game_sub_deadline', models.DateField()),
                ('location', models.CharField(max_length=1024)),
                ('pre_reg_cost', models.FloatField()),
                ('door_cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('gm', models.CharField(max_length=256)),
                ('number_players', models.CharField(max_length=32)),
                ('duration', models.CharField(max_length=64)),
                ('system', models.CharField(max_length=256)),
                ('triggers', models.CharField(max_length=256)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='TimeBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=64)),
                ('sort_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', con.fields.HourField()),
                ('stop', con.fields.HourField()),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='con.Location'),
        ),
        migrations.AddField(
            model_name='game',
            name='time_block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='con.TimeBlock'),
        ),
        migrations.AddField(
            model_name='game',
            name='time_slot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='con.TimeSlot'),
        ),
        migrations.AddField(
            model_name='game',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blockregistration',
            name='time_block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='con.TimeBlock'),
        ),
        migrations.AddField(
            model_name='blockregistration',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
