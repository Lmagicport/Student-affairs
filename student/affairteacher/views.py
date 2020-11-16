from django.shortcuts import render
from .models import StudentTeacher
# Create your views here.


def LookSelf(request, Num):
    try:
        teacher = StudentTeacher.objects.filter(TeaNum=Num)
        teainfo = teacher[0]
        print(teainfo)
        return render(request, 'teacher/Tea_lookself.html', {"teainfo": teainfo})
    except Exception as e:
        file_write = open(r'student/error.txt', 'w')
        file_write.write(e)


def UpdateSelf(request, Num):
    try:
        teacher = StudentTeacher.objects.filter(TeaNum=Num)
        teainfo = teacher[0]
        return render(request, 'teacher/update_self.html',{"teainfo": teainfo})
    except Exception as e:
        file_write = open(r'student/error.text','w')
        file_write.write(e)