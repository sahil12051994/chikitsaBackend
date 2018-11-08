# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-06 12:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvd_portal', '0024_auto_20181101_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='history_high_blood_pressure',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='history_of_diseases',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='history_of_obesity',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='history_of_preeclampsia',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='lmp',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='more_than_one_baby',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='mother_or_sister_had_preeclampsia',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='abdominal_pain',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='bleeding_per_vaginum',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='decreased_fetal_movements',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='diastolic',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='extra_comments',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='headache',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='heart_rate',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='hyper_tension',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='swelling_in_hands_or_face',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='systolic',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='urine_albumin',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='visual_problems',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='weight',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]