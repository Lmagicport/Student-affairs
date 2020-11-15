from django.db import models

# Create your models here.


class StudentStudent(models.Model):
    StuNum = models.CharField(primary_key=True, max_length=10)
    StuName = models.CharField(max_length=10)
    StuAge = models.IntegerField()
    StuSex = models.CharField(max_length=10)
    # StuBirth = models.DateField()
    StuCollege = models.CharField(max_length=10)
    StuPass = models.CharField(max_length=10)
    StuMajor = models.CharField(max_length=10)
    StuGra = models.BooleanField()
    class Meta:
        db_table = 'student'


