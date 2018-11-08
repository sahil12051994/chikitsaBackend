from django.conf.urls import url, include
from rest_framework.authtoken import views
from medicine_reminder.views import *

app_name = 'medicine_reminder'

urlpatterns = [
    url(r'medicines/(?P<pk>[0-9]+)$',MedicineList.as_view()),
    url(r'medicines/add/(?P<pk>[0-9]+)$',MedicineAdd.as_view()),
]
