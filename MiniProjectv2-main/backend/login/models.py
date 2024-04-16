'''from django.db import models

# Create your models here.
class academics(models.Model):
    current_sem=models.IntegerField()
    completed_sem=models.IntegerField()
    cgpa=models.FloatField()
    overall_status=models.TextField()
    attendance_perc=models.FloatField()

class students(models.Model):
    name=models.CharField(max_length=15)
    register_number=models.CharField(max_length=10)
    acad_details=models.OneToOneField(academics,on_delete=models.CASCADE,related_name='academics',null=True)

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import MinValueValidator, MaxValueValidator


DAYS_CHOICE=[('mon','Monday'),('tue','Tuesday'),('wed','Wednesday'),('thu','Thursday'),('fri','Friday'),('sat','Saturday'),]
LEAVE_CHOICE=[('ml','Medical Leave'),('od','On Duty')]

class Department(models.Model):
    dept_id = models.CharField(max_length=20,primary_key = True)
    dept_name = models.CharField(max_length=50)

class Admin(models.Model):
    admin_id = models.CharField(max_length=20,primary_key = True)
    password =models.CharField(max_length=30)

class Class(models.Model):
    class_id = models.CharField(max_length=20,primary_key=True)
    total_students = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(100)])

class Student(models.Model):
    stud_id = models.CharField(max_length=20, primary_key=True)
    s_password = models.CharField(max_length=30)
    in_out = models.CharField(max_length=5)
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    dob = models.DateField(default='1900-01-01') # Add DateField for date of birth (dob)
    phone = models.CharField(max_length=15, default='000-000-0000')
  # Add CharField for phone number
    email = models.EmailField(default='example@example.com')# Add EmailField for email address
    sem = models.IntegerField(default=1)  # Add IntegerField for semester (sem)
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)

class Faculty(models.Model):
    fac_id = models.CharField(max_length=20,primary_key=True)
    f_password = models.CharField(max_length=30)
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    dob = models.DateField(default='1900-01-01') # Add DateField for date of birth (dob)
    phone = models.CharField(max_length=15, default='000-000-0000')
  # Add CharField for phone number
    email = models.EmailField(default='example@example.com')# Add EmailField for email address

class Calender(models.Model):
    i=models.AutoField(primary_key=True)
    dates = models.DateField()
    day = models.CharField(max_length=9,choices=DAYS_CHOICE,default=None,blank=False)

class Course(models.Model):
    course_id = models.CharField(max_length=20,primary_key=True)
    course_name = models.CharField(max_length=50)
    credits = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
class Attendance(models.Model):
    stud_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    fac_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    presence = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(1)])
    periods = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(8)])
    
    class Meta:
        # Define unique constraint
        unique_together = (("stud_id", "course_id", "date"),)

class Slot(models.Model):
    period_id=models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(8)],primary_key=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

class Holiday(models.Model):
    date = models.DateField(primary_key=True)
    description = models.CharField(max_length=100)

class Advisor(models.Model):
    fac_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)

class Leave(models.Model):
    stud_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)
    leave_type = models.CharField(max_length=9,choices=LEAVE_CHOICE,default=None,blank=False)
    approved = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(1)])


class Timetable(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    day = models.CharField(max_length=9, choices=DAYS_CHOICE, default=None, blank=False)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    periods = models.ForeignKey(Slot, on_delete=models.CASCADE)  # Corrected field name

    class Meta:
        unique_together = (("class_id", "course_id", "day", "periods"),)


class Teache(models.Model):
    fac_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    class Meta:
        unique_together = (("course_id", "class_id"),)

class Subject(models.Model):
    subject_name = models.CharField(max_length=50)
    semester = models.IntegerField(validators=[MinValueValidator(1)])
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class Teaches(models.Model):
    fac_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.fac_id} - {self.subject_name}"

class CourseDiary(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    ATTENDANCE_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    ]
    attendance = models.CharField(max_length=10, choices=ATTENDANCE_CHOICES)
    vivamark = models.FloatField()
    OUTPUT_CHOICES = [
        ('Verified', 'Verified'),
        ('Not Verified', 'Not Verified'),
    ]
    output = models.CharField(max_length=12, choices=OUTPUT_CHOICES)
    programname = models.CharField(max_length=100)
    batch = models.IntegerField(choices=[(1, '1'), (2, '2')], null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)'''

from django.db import models
from django.contrib.auth.models import User
from django.db.models import constants,Q,CheckConstraint
from django.core.exceptions import ObjectDoesNotExist

class faculty(models.Model):
    name=models.CharField(max_length=20)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    fid=models.IntegerField()
    CHOICES=(
        ('cse','computer science and engieeering'),
        ('eee','electrical and electronics engineering'),
        ('ece','electronics and communication engineering'),   
    )   
    department=models.CharField(choices=CHOICES,max_length=3)
    dob = models.DateField(default='1900-01-01')
    phone = models.CharField(max_length=15, default='000-000-0000')
    email=models.EmailField(default='arun28@gmail.com')

    def save(self, *args, **kwargs):
        if self.user.id:
            self.fid=self.user.id 
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
       
class students(models.Model):
    sid=models.IntegerField()
    user=models.OneToOneField(User, on_delete=models.CASCADE )
    student_name=models.CharField(max_length=20)
    CHOICES=(
        ('cse','computer science and engieeering'),
        ('eee','electrical and electronics engineering'),
        ('ece','electronics and communication engineering'),   
    )   
    dept_name=models.CharField(choices=CHOICES,max_length=3)
    clas=models.CharField(max_length=10)
    batch_id=models.CharField(max_length=10)
    roll_no=models.IntegerField(default=1)
    dob = models.DateField(default='1900-01-01')
    ktu_id=models.CharField(max_length=10)
    year_of_admission=models.IntegerField(default=2020)
    sem=models.IntegerField(default=1)
    phone = models.CharField(max_length=15, default='000-000-0000')
    email=models.EmailField(default='arun28@gmail.com')
    advisor=models.ForeignKey(faculty,on_delete=models.CASCADE,related_name='advising_students')
    scheme=models.IntegerField(default=2015)
    def save(self, *args, **kwargs):
        if self.user.id:
            self.sid=self.user.id 
        if self.dept_name and self.sem:
            self.clas='S'+str(self.sem)+self.dept_name
        if self.year_of_admission:
            self.batch_id=str(self.year_of_admission)+'-'+str(self.year_of_admission+4)
        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.student_name

class labs(models.Model):
    CHOICES=(
        ('cse','computer science and engieeering'),
        ('eee','electrical and electronics engineering'),
        ('ece','electronics and communication engineering'),   
    )   
    dept_name=models.CharField(choices=CHOICES,max_length=3)
    sem=models.IntegerField(default=1)
    c_code=models.CharField(max_length=7)
    scheme=models.IntegerField(default=4)
    credit=models.IntegerField(default=4)
    faculty_handling=models.ForeignKey(faculty,on_delete=models.CASCADE,related_name='handling_labs')
    batch=models.CharField(max_length=10)
    hours_taken=models.IntegerField(default=0)
    lab_name=models.CharField(max_length=25,default='automatically updated')
    clas=models.CharField(max_length=15,default='automatic')   

    def save(self,*args, **kwargs):
        if self.dept_name and self.sem:
            self.clas='S'+str(self.sem)+self.dept_name
        try:
            labu=labs_in_curriculum.objects.filter(c_code=self.c_code)
            print(labu)
            if labu:
                self.lab_name=labu[0].lab_name
            else:
                self.lab_name='invalid'
        except ObjectDoesNotExist:
            pass
        super().save(*args,**kwargs)

    def __str__(self):
        return self.lab_name+self.batch

class Exam_Marks(models.Model):
    c_code=models.CharField(max_length=7)
    s_ktu_id=models.CharField(max_length=10,default='pta21cs024')
    Ist_algorithm=models.IntegerField(default=30)
    Ist_viva=models.IntegerField(default=20)
    Ist_output=models.IntegerField(default=0)
    Snd_algorithm=models.IntegerField(default=0)
    Snd_viva=models.IntegerField(default=0)
    Snd_output=models.IntegerField(default=0)
    attendance=models.FloatField(default=100.0)
    att_mark=models.IntegerField(default=10)
    Total_internal=models.IntegerField(default=50)
    lab=models.ForeignKey(labs,on_delete=models.CASCADE,related_name='marklists')

class Schedules(models.Model):
    lab=models.ManyToManyField(labs,related_name='schedules')
    matter=models.TextField(max_length=150)
    
class course_record(models.Model):
    date=models.DateField()
    s_name=models.CharField(max_length=20, null=True)
    s_ktu_id=models.CharField(max_length=20,default='PTA21CS001')
    labs_inst=labs.objects.all()
    batch=models.CharField(max_length=10)
    output=models.BooleanField(default=True)
    session_no=models.IntegerField()
    c_code=models.CharField(max_length=7)
    attendance=models.BooleanField(default=True)
    viva_mark=models.IntegerField(default=0)
    exp_no=models.IntegerField(default=0)
    exp_comp=models.IntegerField(default=0)
    next_exp=models.IntegerField(default=0)
    course_diary=models.CharField(max_length=25)
    total_hours=models.IntegerField(default=3)
    presented_hours=models.IntegerField(default=3)
    attendance_perc=models.FloatField(default=0.0)
    class Meta:
        unique_together=('s_name','date')
        constraints=[
            CheckConstraint(
                check=Q(attendance=True) | Q(output=False),
                name='student not present constrain'
            )
        ]
    
    def save(self,*args,**kwargs):
        if self.presented_hours and self.total_hours:
            lab_inst=labs.objects.filter(batch=self.batch)
            try:
                latest_r=course_record.objects.filter(s_ktu_id=self.s_ktu_id).latest('date')
                self.total_hours=latest_r.total_hours+self.total_hours
                self.presented_hours=latest_r.presented_hours+self.presented_hours
                self.attendance_perc=(self.presented_hours/self.total_hours)*100
            except ObjectDoesNotExist:
                self.attendance_perc=(self.presented_hours/self.total_hours)*100
            lab_inst[0].hours_taken=self.total_hours
        super().save(*args,**kwargs)


class labs_in_curriculum(models.Model):
    CHOICES=(
        ('cse','computer science and engieeering'),
        ('eee','electrical and electronics engineering'),
        ('ece','electronics and communication engineering'),   
    )   
    dept_name=models.CharField(choices=CHOICES,max_length=3)
    sem=models.IntegerField(default=1)
    c_code=models.CharField(max_length=8)
    lab_name=models.CharField(max_length=20)
