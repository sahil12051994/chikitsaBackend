# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-04 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvd_portal', '0017_auto_20180702_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='notification_app',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='notifications',
            name='priority',
            field=models.PositiveIntegerField(null=True),
        ),
    ]