from django import forms
from .models import students
#from .models import academics

from django import forms
from .models import students
#from .models import academics

'''class insert_Form(forms.ModelForm):
    current_sem = forms.IntegerField()
    completed_sem = forms.IntegerField()
    cgpa = forms.FloatField()
    overall_status = forms.CharField(widget=forms.Textarea)
    attendance_perc = forms.FloatField()

    class Meta:
        model = students
        fields = '__all__'
        exclude = ['acad_details'] 
    def save(self, commit=True):
        student = super().save(commit=False)
        acad_details = academics.objects.create(
            current_sem=self.cleaned_data['current_sem'],
            completed_sem=self.cleaned_data['completed_sem'],
            cgpa=self.cleaned_data['cgpa'],
            overall_status=self.cleaned_data['overall_status'],
            attendance_perc=self.cleaned_data['attendance_perc']
        )
        student.acad_details = acad_details
        if commit:
            student.save()
        return student'''
from django import forms
from django.contrib import admin
from django.forms import formset_factory
from .models import students,course_record,labs
from django import forms
from .models import course_record

class MyModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MyModelForm, self).__init__(*args, **kwargs)
        self.fields['course_diary'].empty_label = "Select a diary"
        self.fields['date'].widget.attrs['placeholder']="yyyy-mm-dd"
    class Meta:
        model = course_record
        fields = ['date','batch','c_code', 'session_no', 's_name', 'attendance', 'exp_no', 'output', 'presented_hours', 'total_hours', 'course_diary','viva_mark','exp_comp','s_ktu_id']
        labels = {
            'date': '',
            'session_no': '',
            'output': '',
            's_name': '',
            'attendance': '',
            'exp_no': '',
            'next_exp': '',
            'presented_hours':'',
            'total_hours':'',
            'course_diary': '',
            'viva_mark':'',
            'exp_comp':'',
            's_ktu_id':'',
            'c_code':'',    
        }

class classquery(forms.Form): 


    class_s=forms.ChoiceField(choices=[])
    s_no=forms.IntegerField(label='starting roll number')
    e_no=forms.IntegerField(label='ending roll number')

    date=forms.DateField(label='date')
   
    def __init__(self,*args,**kwargs):
        faculty_id=kwargs.pop('faculty_id')
        batchs=kwargs.pop('batches_selected')
        classes=kwargs.pop('classes')
        super(classquery,self).__init__(*args, **kwargs)

        myInstances=students.objects.values('clas').distinct()
        #choices=[(obj.clas,str(obj.clas))for obj in myInstances]
        classes=set(classes)
        choices_c=[(obj,obj)for obj in classes]
        self.fields['class_s'].choices=choices_c
        #[(obj['clas'],str(obj['clas'])) for obj in myInstances]

        #super(classquery, self).__init__(*args,**kwargs)
        
        labInsta=labs.objects.filter(faculty_handling_id=faculty_id,clas__in=classes,batch__in=batchs)
        print(labInsta)
        choices_d=[(obj,f"{obj.lab_name}-{obj.batch}")for obj in labInsta]
        self.fields['diary']=forms.ChoiceField(choices=choices_d)

        self.fields['date'].widget.attrs['placeholder']="yyyy-mm-dd"
        
        unique_batchs=set(batchs)
        choices_b=[(obj,obj) for obj in unique_batchs]
        self.fields['batch']=forms.ChoiceField(choices=choices_b)



