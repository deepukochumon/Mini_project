# Create your views here.
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import get_token
from django.views.decorators.cache import never_cache
from django.core.exceptions import ObjectDoesNotExist,ValidationError
from django.db import IntegrityError
from django.forms import formset_factory
from django.contrib import messages

#from .forms import insert_Form
#from login.models import Student

# views.py
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.permissions import AllowAny
from .serializers import LoginSerializer
from .forms import classquery,MyModelForm
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from .models import Student, Department, Class,Subject
from .models import labs,labs_in_curriculum,students,faculty,course_record
from .serializers import attendance_query_serializer

fac=None
dep=""
cla=""
cou=""
sem=""
stu=""

def fac_initial(facl,dept):
    global fac,dep
    fac=facl
    dep=dept
    print('name is',fac.id)
    return


def initial(fact,dept,sems):
    global stu,dep,sem
    stu=fact
    dep=dept
    sem=sems
    return

def tial(clat,cout):
    global cla,cou
    cla=clat
    cou=cout
    return

@api_view(['GET'])
def fac_data_view(request):
    # Fetch the user data based on the authenticated user
    #facult = get_object_or_404(faculty, fac_id=fac)
    print(fac)
    user_data = {
        "name": fac.name,
        "department": fac.department,
        "id":fac.fid,
        "dob": fac.dob.strftime('%Y-%m-%d'),  # Format dob as YYYY-MM-DD string
        "phone": fac.phone,
        "email": fac.email,    
    }

    return Response(user_data)

@api_view(['GET'])
def get_lab_details(request):
    print('faculty is',fac)
    labses = labs.objects.filter(faculty_handling=fac.id)
    print(labses)

    lab_names = [lab.lab_name for lab in labses]
    print(lab_names)

    return Response({"lab_names": lab_names})

@api_view(['GET'])
def user_data_view(request):
    # Fetch the user data based on the authenticated user
    #student = get_object_or_404(students, stud_id=fac)

    user_data = {
        "name": stu.student_name,
        "department": stu.dept_name,
        "class": stu.clas,
        "dob": stu.dob.strftime('%Y-%m-%d'),  # Format dob as YYYY-MM-DD string
        "phone": stu.phone,
        "email": stu.email,
        "sem": stu.sem,
    }
    return Response(user_data)


@api_view(['GET'])
def s_get_lab_details(request):
    
     Labs = labs_in_curriculum.objects.filter(semester=sem, department=dep)

     lab_names = [lab.lab_name for lab in Labs]
     print(lab_names)

     return Response({"lab_names": lab_names})
    

@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def login_view1(request):
    if request.method == 'POST':
        print("hello")  # Print "hello" when the POST request is received

        # Your existing code to handle the POST request
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            user_type = serializer.validated_data.get('user_type')
            std=students.objects.filter(stud_id=username)

            if std.exists():
                print("user exists")
                if std.get().s_password==password:
                     d=std.get().dept_id.dept_id
                     sem=std.get().sem
                     initial(username,d,sem)
                     return Response({'redirect_url':'http://localhost:3000/home/'})
                else:
                    return Response({'message':'invalid credentials'},status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message':'invalid credentials'},status=status.HTTP_400_BAD_REQUEST)
                    

            

            # Rest of your code...
            # ...

        return Response(status=status.HTTP_200_OK)

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
                facl=faculty.objects.filter(user=user)
                print(facl[0].name)
                d=facl[0].department
                fac_initial(facl[0],d)
                print('faculty authenticated')
                return Response({'redirect_url':'http://localhost:3000/faculty_home/'})
            else:
                return Response({'message':'invalid credentials'},status=status.HTTP_400_BAD_REQUEST)
            
        elif usertype=='student':
            user=authenticate(request,username=username,password=password)
            if user is not None and not user.is_staff:
                std=students.objects.filter(user=user)
                d=std[0].dept_name
                sem=std[0].sem
                login(request,user)
                initial(std[0],d,sem)
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
    pass


@api_view(['GET','POST'])
@ensure_csrf_cookie
def attendance_query(request):
    try:
        facult=faculty.objects.first() #this change the user
        facult_id = facult.id
        print(fac)
        diaries=labs.objects.filter(faculty_handling=facult_id)
        #print('batches are', batches)
        classes=[obj.clas for obj in diaries if obj.clas]
        batches=[obj.batch for obj in diaries if obj.batch]
        diaries=[obj.id for obj in diaries if obj]
        print(batches)
    except ObjectDoesNotExist:
        return HttpResponse('not found')
    if request.method=='POST':
        frm=classquery(request.POST,faculty_id=facult_id,batches_selected=batches,classes=classes)
        if frm.is_valid():
            batch=frm.cleaned_data['batch']
            cass_s=frm.cleaned_data['class_s']
            s_no=frm.cleaned_data['s_no']
            e_no=frm.cleaned_data['e_no']
            diary=frm.cleaned_data['diary']
            date=frm.cleaned_data['date']
            return redirect('marking',batch=batch,class_s=cass_s,s_no=s_no,e_no=e_no,diary=diary,date=date)
        else:
            return Response(frm.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
       # frm=classquery(faculty_id=facult_id,batches_selected=batches,classes=classes)
    #return render(request,'attend.html',{'frm':frm})
        print('faculyt is',facult_id)
        print('batches are ',batches)
        print('classes are ',classes)
        frm = attendance_query_serializer(faculty_id=facult_id, batches_selected=list(batches), classes=list(classes),diaries=list(diaries))
        print(frm.data)
        return Response(frm.data,status=status.HTTP_400_BAD_REQUEST)


def create_multiple_instances(request,batch,class_s,s_no,e_no,diary,date):
    batch_selected=batch 
    diary_selected=diary
    date_error='Course_record with this Name and Date already exists.'
    stud=[]
    students_objs=students.objects.filter(batch_id=batch_selected)
    students_objs=students_objs.filter(clas=class_s)
    for obj in students_objs:
        if obj.roll_no<=e_no and obj.roll_no>=s_no:
            stud.append(obj)
    ext=len(stud)
    stud.sort(key=lambda x: x.roll_no)
    MyModelFormSet = formset_factory(MyModelForm, extra=ext)  # Change extra to the desired number of forms
    formset=MyModelFormSet()
    if request.method == 'POST':
        if 'submit_button' in request.POST:
            formset = MyModelFormSet(request.POST)
            invalid_form=[]
            if formset.is_valid():
                all_valid=True
                instances_to_save = []
                for form in formset:
                    instance_data = form.cleaned_data
                    instance_data['course_diary'] = diary_selected
                    if instance_data['output']:
                        instance_data['exp_comp'] = instance_data['exp_no']
                        instance_data['next_exp'] = instance_data['exp_no'] + 1
                    else:
                        instance_data['next_exp'] = instance_data['exp_no']
                    instance = course_record(**instance_data)
                    # Run model validation without saving
                    try:
                        instance.full_clean()
                        instances_to_save.append(instance)
                    except ValidationError as e:
                        print('phase 1')
                        all_valid=False
                print('reached')
                if all_valid:
                    messages.success(request,'successfully modified')
                    if instances_to_save:
                        try: 
                            course_record.objects.bulk_create(instances_to_save)
                            print('save reached')
                        except IntegrityError as e:
                            error_msg='integrity error caught:{}'.format(str(e))
                            print('integrity error phase 2 catched ')
                            return render(request, 'index.html', {'formset':formset, 'error_msg': error_msg})
                    return redirect('querying')
            else:
                print('not valid')
                for form in formset:
                    if form.errors:
                        print(f"Errors for form {form.prefix}: {form.errors}")
                for form in formset:
                    for field, errors in form.errors.items():
                        if date_error in errors:
                            invalid_form.append((form.cleaned_data.get('date'),form.cleaned_data.get('name')))
                            print(form.cleaned_data['date'])
                            print(f"Field: {field}, Errors: {', '.join(errors)}")
                        # Print field name and associated errors
                return render(request, 'index.html', {'formset': formset, 'invalid_form':invalid_form})
        elif 'exit_button' in request.POST:
            return redirect('querying')
        
    formset = MyModelFormSet()
    i=0
    for form in formset.forms:
        val=stud[i].student_name
        form.initial['s_name']=val
        form.initial['course_diary']=diary_selected
        form.initial['date']=date
        form.initial['s_ktu_id']=stud[i].ktu_id
        form.initial['batch']=batch_selected
        l_name=diary_selected[:-9]
        l_obj=labs_in_curriculum.objects.filter(lab_name=l_name)

        form.initial['c_code']=l_obj[0].c_code
        print(stud[i].ktu_id)
        try:
            latest_r=course_record.objects.filter(s_name=val,course_diary=diary_selected)
            latest_r=latest_r.latest('date')
            form.initial['exp_comp']=latest_r.exp_comp
            form.initial['session_no']=latest_r.session_no+1
            form.initial['exp_no']=latest_r.exp_comp+1
            form.initial['next_exp']=latest_r.exp_comp+1
            print('previous value set')
        except ObjectDoesNotExist:
            form.initial['exp_comp']=0
            form.initial['exp_no']=1
            form.initial['session_no']=1
            form.initial['next_exp']=0
            print('default assigned')
        i=i+1
    return render(request, 'index.html', {'formset': formset})