# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-06 12:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_reminder', '0007_auto_20181106_1813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='medicine_end',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='medicine',
            old_name='medicine_extra_comments',
            new_name='extra_comments',
        ),
        migrations.RenameField(
            model_name='medicine',
            old_name='medicine_freq',
            new_name='freq',
        ),
        migrations.RenameField(
            model_name='medicine',
            old_name='medicine_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='medicine',
            old_name='medicine_start',
            new_name='start',
        ),
    ]
