from django.urls import path
from . import views
from login.views import login_view

urlpatterns = [
    path('hello-world/', views.hello_world, name='hello_world'),
    path('login/',login_view, name='login_view'),
]