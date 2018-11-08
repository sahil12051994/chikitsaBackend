# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-06 12:40
from __future__ import unicode_literals

import cvd_portal.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cvd_portal', '0025_auto_20181106_1810'),
        ('medicine_reminder', '0005_auto_20180705_0411'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('byte', models.TextField()),
                ('medicine_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='medicine_reminder.Medicine')),
                ('extra_comments_image', models.TextField(default='')),
                ('time_stamp', cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='doctorinchikitsadata',
            name='doctor_id',
        ),
        migrations.RemoveField(
            model_name='reminderdataforparticularmed',
            name='medicine',
        ),
        migrations.RemoveField(
            model_name='reminderdataforparticularmed',
            name='patient_id',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='compunds',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='medicine_Image',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='name',
        ),
        migrations.AddField(
            model_name='medicine',
            name='medicine_end',
            field=cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='medicine',
            name='medicine_extra_comments',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='medicine',
            name='medicine_freq',
            field=models.CharField(default='DAILY', max_length=50),
        ),
        migrations.AddField(
            model_name='medicine',
            name='medicine_name',
            field=models.CharField(default='No Name', max_length=50),
        ),
        migrations.AddField(
            model_name='medicine',
            name='medicine_start',
            field=cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='medicine',
            name='patient_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cvd_portal.Patient'),
        ),
        migrations.DeleteModel(
            name='DoctorInChikitsaData',
        ),
        migrations.DeleteModel(
            name='ReminderDataForParticularMed',
        ),
    ]
