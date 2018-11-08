# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import datetime
from dateutil import tz
from cvd_portal.models import *

class Medicine(models.Model):
    patient_id = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        null=True
    )
    medicine_name = models.CharField(max_length=50, default="No Name")
    medicine_freq = models.CharField(max_length=50, default="DAILY")
    medicine_extra_comments = models.TextField(default="")
    medicine_start = CustomDateTimeField(default=datetime.datetime.now)
    medicine_end = CustomDateTimeField(default=datetime.datetime.now)
    time_stamp = CustomDateTimeField(default=datetime.datetime.now)
    medicine_Image = models.TextField(default="")

class PatientInChikitsaData(models.Model):
    problems_faced = models.TextField()
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patientInChikitsaData')
    next_visit = CustomDateTimeField(default=datetime.datetime.now)
    doctor_comments = models.TextField()
