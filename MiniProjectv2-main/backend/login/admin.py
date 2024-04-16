import csv
from django.contrib import admin
from django.http import HttpResponse
#from .models import Department, Class, Student, Faculty, Attendance,Subject,Teaches,CourseDiary


'''class AttendanceAdmin(admin.ModelAdmin):
    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="AttendanceReport.csv"'
        writer = csv.writer(response)
        writer.writerow(['Stud-Id', 'Faculty-Id', 'Dept', 'Course-Id', 'Date(dd-mm-yyyy)', 'Status'])
        for obj in queryset:
            status = 'Present' if obj.presence else 'Absent'
            writer.writerow([obj.stud_id.stud_id, obj.fac_id.fac_id, obj.stud_id.dept_id.dept_id,
                             obj.course_id.course_id, obj.date, status])
        return response

    export_to_csv.short_description = 'Export to CSV'

    list_display = ('stud_id', 'fac_id', 'course_id', 'date', 'presence')
    actions = [export_to_csv]





admin.site.register(Department)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Subject)
admin.site.register(Teaches)
admin.site.register(CourseDiary)'''

# Register your models here.
from django.contrib import admin

from .models import Schedules,Exam_Marks,course_record,students,course_record,faculty,labs,labs_in_curriculum

# Register your models here.


class LabsAdmin(admin.ModelAdmin):
    list_display = ('lab_name', 'dept_name', 'sem', 'c_code', 'faculty_handling', 'batch', 'hours_taken', 'clas')
    list_filter = ('dept_name', 'sem', 'faculty_handling', 'batch')
    search_fields = ('lab_name', 'c_code', 'faculty_handling__name') # Assuming faculty has a name field

admin.site.register(labs, LabsAdmin)

class labs_in_curriculumAdmin(admin.ModelAdmin):
    list_display=('dept_name','sem','c_code','lab_name')
admin.site.register(labs_in_curriculum,labs_in_curriculumAdmin)

class studAdmin(admin.ModelAdmin):
    list_display = ['sid', 'student_name', 'dept_name', 'clas', 'batch_id', 'roll_no', 'dob', 'ktu_id', 'year_of_admission', 'sem', 'phone', 'email', 'advisor', 'scheme']
    def class_sec(self,obj):
        return obj.clas
admin.site.register(students, studAdmin)

class CourseRecordAdmin(admin.ModelAdmin):
    list_display = ['date', 's_name', 'output', 'session_no', 'c_code', 'attendance', 'viva_mark', 'exp_no', 'exp_comp', 'next_exp', 'course_diary', 'total_hours', 'presented_hours','attendance_perc']
    list_filter = ['date', 'c_code', 'attendance', 'output']
    search_fields = ['s_name', 'c_code', 'course_diary']

admin.site.register(course_record, CourseRecordAdmin)


class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name', 'fid', 'department', 'dob', 'phone', 'email']
    list_filter = ['department']
    search_fields = ['name', 'fid', 'department']

admin.site.register(faculty, FacultyAdmin)

class ExamMarksAdmin(admin.ModelAdmin):
    list_display = ['c_code', 'Ist_algorithm', 'Ist_viva', 'Ist_output', 'Snd_algorithm', 'Snd_viva', 'Snd_output', 'attendance', 'att_mark', 'Total_internal']
    list_filter = ['c_code']
    search_fields = ['c_code']

admin.site.register(Exam_Marks, ExamMarksAdmin)

class LabInline(admin.TabularInline):
    model = Schedules.lab.through
    extra = 1

class SchedulesAdmin(admin.ModelAdmin):
    list_display = ['matter']
    search_fields = ['matter']
    inlines = [LabInline]

admin.site.register(Schedules, SchedulesAdmin)


