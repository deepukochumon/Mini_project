from django.urls import path,include
from . import views
from login.views import login_view
from login.views import user_data_view,s_get_lab_details,create_multiple_instances,attendance_query,fac_data_view,get_lab_details

urlpatterns = [
    path('hello-world/', views.hello_world, name='hello_world'),
    path('login/',login_view, name='login_view'),
    path('user-data/', user_data_view, name="user-data"),
    path('lab-details/', s_get_lab_details, name="s_get_lab_details"),
    path('hel/<str:batch>/<str:class_s>/<int:s_no>/<int:e_no>/<str:diary>/<str:date>',create_multiple_instances, name='marking'),
    path('attendance_query/',attendance_query, name='querying'),
    path('fac_data_get/',fac_data_view),
    path('get_lab_details/',get_lab_details)
    #path('',include('checkmodel.urls'))
]