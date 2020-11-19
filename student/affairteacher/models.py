from datetime import date
from django.db import models
import datetime
# Create your models here.


class StudentTeacher(models.Model):
    TeaNum = models.CharField(primary_key=True, max_length=10)
    TeaName = models.CharField(max_length=10)
    TeaPass = models.CharField(max_length=10)
    TeaCollege = models.CharField(max_length=10)
    TeaMajor = models.CharField(max_length=10)
    TeaSex = models.CharField(max_length=10)
    TeaBirth = models.DateField(default=datetime.datetime.now().date())
    class Meta:
        db_table = 'teacher'
    def __str__(self) -> str:
        return self.TeaName


