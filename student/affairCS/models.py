from django.db import models

# Create your models here.


class StudentTeacher(models.Model):
    StuNum = models.CharField(max_length=10)
    StuName = models.CharField(max_length=10)
    CourNum = models.IntegerField(max_length=10)
    CourName = models.CharField(max_length=10)
    CourGrade = models.FloatField(default=0)
    CourTea = models.CharField(max_length=10)

    class Meta:
        db_table = 'student-course'
