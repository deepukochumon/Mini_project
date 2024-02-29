# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import get_token
from django.views.decorators.cache import never_cache
from .models import students
from .forms import insert_Form

# views.py
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.permissions import AllowAny

from .serializers import LoginSerializer
@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def login_view(request):
    # Handle user login logic here
    serializer=LoginSerializer(data=request.data)
    if serializer.is_valid():
        username=serializer.validated_data.get('username')
        password=serializer.validated_data.get('password')
        usertype=serializer.validated_data.get('user_type')

        if usertype=='faculty':
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_staff:
                login(request,user)
                print('faculty authenticated')
                return Response({'redirect_url':'http://localhost:3000/faculty_home/'})
            else:
                return Response({'message':'invalid credentials'},status=status.HTTP_400_BAD_REQUEST)
            
        elif usertype=='student':
            user=authenticate(request,username=username,password=password)
            if user is not None and not user.is_staff:
                login(request,user)
                print('student authenticated')
                return Response({'redirect_url':'http://localhost:3000/home/'})
            else:
                return Response({'message':'Invalid credentials'},status=status.HTTP_400_BAD_REQUEST)
                
    return Response(status=status.HTTP_200_OK)


def home_view(request):
    try:
        username=request.GET.get('variable')
        student_data=students.objects.get(name=username)
        return render(request,'student.html',{'student_data':student_data})
    except students.DoesNotExist:
        # Handle the case when the student with the given username is not found
        return redirect('login')

def fhome_view(request):
    return render(request,'faculty.html')

def authlogout(request):
    return redirect('login')

def insert_data(request):
    if request.method == 'POST':
        frm=insert_Form(request.POST)
        if frm.is_valid():
            frm.save()
    frm=insert_Form()
    return render(request,'create.html',{'frm':frm})