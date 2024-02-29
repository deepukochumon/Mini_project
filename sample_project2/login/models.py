from django.db import models

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