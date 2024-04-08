from django.db import models
from django.contrib.auth.models import User
from django.db.models import constants,Q,CheckConstraint


class faculty(models.Model):
    name=models.CharField(max_length=20)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    fid=models.IntegerField()

    def save(self, *args, **kwargs):
        if self.user.id:
            self.fid=self.user.id 
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class course(models.Model):
    c_code=models.CharField(max_length=6)
    c_name=models.CharField(max_length=20)
    credit=models.IntegerField()
    faculty=models.ManyToManyField(faculty,related_name='handling_course')
    sem=models.IntegerField()
    CHOICES=(
        ('cse','computer science and engieeering'),
        ('eee','electrical and electronics engineering'),
        ('ece','electronics and communication engineering'),   
    )   
    dept_name=models.CharField(choices=CHOICES,max_length=3)

class class_section(models.Model):
    c_id=models.CharField(max_length=7)
    number_of_students=models.IntegerField()
    sem=models.CharField(max_length=2)
    advisor=models.ForeignKey(faculty,on_delete=models.CASCADE,related_name='advising_class',null=True)
    CHOICES=(
        ('cse','computer science and engieeering'),
        ('eee','electrical and electronics engineering'),
        ('ece','electronics and communication engineering'),   
    )   
    dept_name=models.CharField(choices=CHOICES,max_length=3)

    def save(self,*args,**kwargs):
        self.c_id=self.dept_name+'S'+self.sem
        super().save(*args,**kwargs)

    def __str__(self):
        return self.c_id
    

class Batch(models.Model):
    name=models.CharField(max_length=8, null=True)

    def __str__(self):
        return self.name

class students(models.Model):
    student_name=models.CharField(max_length=20)
    roll_no=models.IntegerField(default=1)
    register_no=models.CharField(max_length=10)
    user=models.OneToOneField(User, on_delete=models.CASCADE )
    batch_set=models.ForeignKey(Batch, on_delete=models.CASCADE, null=True, related_name='students')
    batch_id=models.IntegerField()
    clas=models.ForeignKey(class_section,on_delete=models.CASCADE,related_name='students_of_this',null=True)
    sid=models.IntegerField()
    def save(self, *args, **kwargs):
        if self.user.id:
            self.sid=self.user.id 
        if self.batch_set.id:
            self.batch_id=self.batch_set.id
        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.student_name


class lab(models.Model):
    lab_name=models.CharField(max_length=15)
    course=models.OneToOneField(course,on_delete=models.CASCADE,related_name='lab_session',null=True)
    
    def __str__(self):
        return self.lab_name

class Course_diary(models.Model):
    facul_in=models.ForeignKey(faculty,on_delete=models.CASCADE,related_name='course_dia',null=True,default=None,to_field='id')
    batches=models.ForeignKey(Batch,on_delete=models.CASCADE, related_name='batch', null=True)
    batch_id=models.IntegerField(null=True)
    lab_name=models.ForeignKey(lab,on_delete=models.CASCADE,related_name='diary',null=True)

    def save(self, *args, **kwargs):
        if self.batches.id:
            self.batch_id=self.batches.id
        super().save(*args,**kwargs)
    
    def __str__(self):
        return str(self.lab_name)
    
    class Meta:
        unique_together=('batches','lab_name')
    
class course_record(models.Model):
    name=models.CharField(max_length=20, null=True)
    date=models.DateField()
    session_no=models.IntegerField()
    attendance=models.BooleanField(default=True)
    output=models.BooleanField(default=True)
    exp_no=models.IntegerField(default=0)
    diary=models.ForeignKey(Course_diary, on_delete=models.CASCADE, related_name='course_diary', null=True)
    exp_comp=models.IntegerField(default=0)
    next_exp=models.IntegerField(default=0)
    viva_mark=models.IntegerField(default=0)


    class Meta:
        unique_together=('name','date')
        constraints=[
            CheckConstraint(
                check=Q(attendance=True) | Q(output=False),
                name='student not present constrain'
            )
        ]


