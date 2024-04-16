from django.contrib import admin
from django.urls import path,include
from .views import get_attendance_data #fac_login,fac_data_view,get_lab_details

urlpatterns = [
    #path('fac_login/', fac_login, name="user-fac_login"),
    #path('fac_data_get/', fac_data_view, name="fac_data_view"),
    #path('get_lab_details/', get_lab_details, name="get_lab_details"),
    path('get_attendance_data/', get_attendance_data, name="get_attendance_data"),
]