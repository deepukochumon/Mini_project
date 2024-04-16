# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import get_token
from django.views.decorators.cache import never_cache

#from login.models import Student,CourseDiary

# views.py
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.permissions import AllowAny
from .serializers import LoginSerializer

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from login.models import Student, Department, Class,Subject,Faculty,Teaches

'''fac=""
dep=""
cla=""
cou=""
sem=""


def initial(fact,dept):
    global fac,dep
    fac=fact
    dep=dept

    return


@api_view(['GET'])
def fac_data_view(request):
    # Fetch the user data based on the authenticated user
    student = get_object_or_404(Faculty, fac_id=fac)

    user_data = {
        "name": f"{student.f_name} {student.l_name}",
        "department": student.dept_id.dept_name,
        "id":fac,

        "dob": student.dob.strftime('%Y-%m-%d'),  # Format dob as YYYY-MM-DD string
        "phone": student.phone,
        "email": student.email,
        
    }

    return Response(user_data)



@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def fac_login(request):
    if request.method == 'POST':
        print("hello")  # Print "hello" when the POST request is received

        # Your existing code to handle the POST request
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')

            facl=Faculty.objects.filter(fac_id=username)

            if facl.exists():
                print("user exists")
                if facl.get().f_password==password:
                     d=facl.get().dept_id.dept_id
                     
                     initial(username,d)
                     return Response({'redirect_url':'http://localhost:3000/faculty_home/'})
                else:
                    return Response({'message':'invalid credentials'},status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message':'invalid credentials'},status=status.HTTP_400_BAD_REQUEST)
                    

            

            # Rest of your code...
            # ...

        return Response(status=status.HTTP_200_OK)
    
@api_view(['GET'])
def get_lab_details(request):
    
     labs = Teaches.objects.filter(fac_id=fac)

     lab_names = [lab.subject_name for lab in labs]
     print(lab_names)

     return Response({"lab_names": lab_names})'''

@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def get_attendance_data(request):
    pass
    '''if request.method == 'POST':
        # Get the parameters from the POST request data
        date = request.data.get('date')
        subject_name = request.data.get('class')
        batch = request.data.get('batch')
        print(date)
        print(subject_name)
        print(batch)

        # Filter the CourseDiary model based on the provided parameters
        attendance_data = CourseDiary.objects.filter(
            date=date,
            subject__subject_name=subject_name,
            batch=batch
        )

        # Serialize the filtered data
        serialized_data = [
            {
                'date': data.date,
                'subject_name': data.subject.subject_name,
                'student_name': data.student.stud_id,
                'batch': data.batch,
                'attendance': data.attendance,
                'vivamark': data.vivamark,
                'output': data.output,
                'programname': data.programname
            }
            for data in attendance_data
        ]

        # Return the serialized data as a JSON response
        return JsonResponse({'attendance_data': serialized_data})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)'''