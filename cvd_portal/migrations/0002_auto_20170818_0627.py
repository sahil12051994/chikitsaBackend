# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 06:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvd_portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='designation',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='hospital',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='mobile',
            field=models.IntegerField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='speciality',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='mobile',
            field=models.IntegerField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='patientdata',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 18, 6, 27, 53, 826299)),
        ),
    ]