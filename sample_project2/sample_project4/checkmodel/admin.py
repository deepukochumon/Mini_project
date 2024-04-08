
# Register your models here.
from django.contrib import admin

from .models import Course_diary,Batch,students,course_record,faculty,class_section,lab,course

# Register your models here.

class CDA(admin.ModelAdmin):
    list_display=('name',)
admin.site.register(Batch, CDA)

admin.site.register(lab)
admin.site.register(course)

class studAdmin(admin.ModelAdmin):
    list_display=('student_name','batch_set','register_no','sid','class_sec')
    def class_sec(self,obj):
        return obj.clas.c_id
admin.site.register(students, studAdmin)

class BDA(admin.ModelAdmin):
    list_display=('name','date','attendance','session_no','exp_no','output','exp_comp','next_exp','diary','viva_mark')
admin.site.register(course_record, BDA)

class course_d(admin.ModelAdmin):
    list_display=('batch_id','facul_in','lab_name','batches')
admin.site.register(Course_diary, course_d)

class fac_data(admin.ModelAdmin):
    list_display=('name','user','fid')
admin.site.register(faculty,fac_data)

class class_data(admin.ModelAdmin):
    list_display=('c_id','number_of_students','sem','advisor','dept_name')
admin.site.register(class_section,class_data)