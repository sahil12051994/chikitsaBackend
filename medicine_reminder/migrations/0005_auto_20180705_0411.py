# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-04 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_reminder', '0004_auto_20180703_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificationinchikitsa',
            name='notification_id',
        ),
        migrations.RenameField(
            model_name='reminderdataforparticularmed',
            old_name='timings_of_intake',
            new_name='start_time',
        ),
        migrations.AddField(
            model_name='reminderdataforparticularmed',
            name='extra_comments',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='reminderdataforparticularmed',
            name='times',
            field=models.PositiveIntegerField(default=1, null=True),
        ),
        migrations.DeleteModel(
            name='NotificationInChikitsa',
        ),
    ]
