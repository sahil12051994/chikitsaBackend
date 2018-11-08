from rest_framework import serializers
from medicine_reminder.models import *
from cvd_portal.serializers import DynamicFieldsModelSerializer,PatientSerializer1
from django.contrib.auth.models import User

# to get the list of medicines starting containing letter
class MedicineSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Medicine
        fields = [
            'pk',
            'medicine_name',
            'medicine_freq',
            'medicine_extra_comments',
            'medicine_start',
            'medicine_end',
            'medicine_Image'
            ]

# to read data of single medicine
class MedicineDataAddSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Medicine
        fields = [
            'medicine_name',
            'medicine_freq',
            'medicine_extra_comments',
            'medicine_start',
            'medicine_end',
            'medicine_Image',
            'patient_id'
        ]

# CRUD Patient data
class PatientDataCRUDSerializer(DynamicFieldsModelSerializer):
    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all())
    all_medicines = serializers.SerializerMethodField('getAllMedicinesData')
    class Meta:
        model = PatientInChikitsaData
        fields = [
            'pk',
            'patient_id',
            'next_visit',
            'doctor_comments',
            'problems_faced',
            'all_medicines'
        ]

    def getAllMedicinesData(self, obj):
        q2set = Medicine.objects.all().filter(reminderdataforparticularmed__patient_id = obj.patient_id).distinct()
        ser = MedicineSerializer(q2set, many=True ,read_only = True)
        return ser.data
