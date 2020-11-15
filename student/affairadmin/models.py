from django.db import models

# Create your models here.


class StudentAdmin(models.Model):
    AdminUser = models.CharField(max_length=5)
    AdminPass = models.CharField(max_length=10, default='123456')
    AdminCollege = models.CharField(max_length=10, default='hbu')
    class Meta:
        db_table = 'admin'


