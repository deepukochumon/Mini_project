from django import forms
from django.contrib import admin
from django.forms import formset_factory
from .models import Course_diary, Batch, students,course_record,class_section
from django import forms
from .models import course_record

class MyModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MyModelForm, self).__init__(*args, **kwargs)
        self.fields['diary'].empty_label = "Select a diary"
        self.fields['date'].widget.attrs['placeholder']="yyyy-mm-dd"
    class Meta:
        model = course_record
        fields = ['date', 'session_no', 'name', 'attendance', 'exp_no', 'output', 'exp_comp', 'next_exp', 'diary','viva_mark']
        labels = {
            'date': '',
            'session_no': '',
            'output': '',
            'name': '',
            'attendance': '',
            'exp_comp': '',
            'exp_no': '',
            'next_exp': '',
            'diary': '',
            'viva_mark':''
        }

class classquery(forms.Form): 
    myInstances=class_section.objects.all()
    choices=[(obj.c_id,str(obj.c_id))for obj in myInstances]

    class_s=forms.ChoiceField(choices=choices)
    s_no=forms.IntegerField(label='starting roll number')
    e_no=forms.IntegerField(label='ending roll number')

    date=forms.DateField(label='date')
   
    def __init__(self,*args,**kwargs):
        faculty_id=kwargs.pop('faculty_id')
        batchs=kwargs.pop('batches_selected')
        super(classquery, self).__init__(*args,**kwargs)
        
        diaryInsta=Course_diary.objects.filter(facul_in_id=faculty_id,batches__in=batchs)
        choices_d=[(obj.id,f"{obj.lab_name.lab_name}-{obj.batches.name}")for obj in diaryInsta if obj.lab_name]

        self.fields['diary']=forms.ChoiceField(choices=choices_d)
        self.fields['date'].widget.attrs['placeholder']="yyyy-mm-dd"
        unique_batchs=set(batchs)
        choices_b=[(obj.name,obj.name) for obj in unique_batchs]
        self.fields['batch']=forms.ChoiceField(choices=choices_b)



