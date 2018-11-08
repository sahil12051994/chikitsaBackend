# -*- coding: utf-8 -*-
from cvd_portal.models import Patient
from medicine_reminder.models import *
from medicine_reminder.serializers import *

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse

from rest_framework.exceptions import ParseError
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from cvd_portal.fcm import send_message
from random import randint

# to get the list of medicines starting containing letter
class MedicineList(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

    def get(self, request, pk):
        d = Medicine.objects.filter(patient_id=pk).order_by('-time_stamp').values()
        print(d.values())
        dataToSend = MedicineSerializer(d, many=True).data
        return JsonResponse(
            dataToSend,
            safe=False,content_type='application/json')

class MedicineAdd(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Medicine.objects.all()
    serializer_class = MedicineDataAddSerializer


# CRUD Patient data
class PatientDataInChikitsa(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = PatientInChikitsaData.objects.all()
    serializer_class = PatientDataCRUDSerializer
