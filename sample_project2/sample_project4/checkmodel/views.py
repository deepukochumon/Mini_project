from django.shortcuts import render,redirect,HttpResponse
from django.forms import formset_factory
from .forms import MyModelForm,classquery
from checkmodel.models import students,course_record,Course_diary,Batch
from django.core.exceptions import ObjectDoesNotExist,ValidationError
from django.db import IntegrityError
from django.contrib.auth.models import User
from .models import faculty
from django.contrib import messages
from django.urls import reverse

def attendance_query(request):
    try:
        current_user=faculty.objects.get(id=1) #this change the user
        facult_id = current_user.id
        batches=Batch.objects.filter(batch__facul_in=facult_id)
    except ObjectDoesNotExist:
        return HttpResponse('not found')
    if request.method=='POST':
        frm=classquery(request.POST,faculty_id=facult_id,batches_selected=batches)
        if frm.is_valid():
            batch=frm.cleaned_data['batch']
            cass_s=frm.cleaned_data['class_s']
            s_no=frm.cleaned_data['s_no']
            e_no=frm.cleaned_data['e_no']
            diary=frm.cleaned_data['diary']
            date=frm.cleaned_data['date']
        return redirect('marking',batch=batch,class_s=cass_s,s_no=s_no,e_no=e_no,diary=diary,date=date)
    else:
        frm=classquery(faculty_id=facult_id,batches_selected=batches)
    return render(request,'attend.html',{'frm':frm})



def create_multiple_instances(request,batch,class_s,s_no,e_no,diary,date):
    try:
        batch_selected=Batch.objects.get(name=batch) 
        diary_selected=Course_diary.objects.get(id=diary)
    except (Course_diary.DoesNotExist, Batch.DoesNotExist) as e:
        return HttpResponse('{}not found'.format(str(e)))
    date_error='Course_record with this Name and Date already exists.'
    stud=[]
    students_objs=batch_selected.students.all()
    students_objs=students_objs.filter(clas__c_id=class_s)
    for obj in students_objs:
        if obj.roll_no<=e_no and obj.roll_no>=s_no:
            stud.append(obj)
    ext=len(stud)
    stud.sort(key=lambda x: x.roll_no)
    print(stud)
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
                    instance_data['diary'] = diary_selected
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
                        all_valid=False
                        print('phase 1')
                print('reached')
                if all_valid:
                    messages.success(request,'successfully modified')
                    if instances_to_save:
                        try: 
                            course_record.objects.bulk_create(instances_to_save)
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
        form.initial['name']=val
        form.initial['diary']=diary_selected
        form.initial['date']=date
        try:
            latest_r=course_record.objects.filter(name=val,diary=diary_selected)
            latest_r=latest_r.latest('date')
            form.initial['exp_comp']=latest_r.exp_comp
            form.initial['session_no']=latest_r.session_no+1
            form.initial['exp_no']=latest_r.exp_comp+1
            form.initial['next_exp']=latest_r.exp_comp+1
            print('experiment number updated')
            print('previous value set')
        except ObjectDoesNotExist:
            form.initial['exp_comp']=0
            form.initial['exp_no']=1
            form.initial['session_no']=1
            form.initial['next_exp']=0
            print('default assigned')
            pass
        i=i+1
    return render(request, 'index.html', {'formset': formset})