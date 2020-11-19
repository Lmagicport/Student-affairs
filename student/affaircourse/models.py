from django.db import models
# Create your models here.


class StudentCourse(models.Model):
    id = models.IntegerField(primary_key=True, max_length=10)
    CourName = models.CharField(max_length=10)
    CourCredit = models.FloatField(max_length=10)
    CourPlace = models.CharField(max_length=10)
    CourType = models.CharField(max_length=10)
    CourReq = models.CharField(max_length=10)
    CourTea = models.CharField(max_length=10)
    CourNum = models.IntegerField()
    Ispass = models.BooleanField(default=False)

    class Meta:
        db_table = 'course'
    
    def __str__(self):
        return "{} {}".format(self.CourName,self.CourCredit)

