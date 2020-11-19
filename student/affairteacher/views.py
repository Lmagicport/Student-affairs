from django.db import models
from django.shortcuts import render
from .models import StudentTeacher
import datetime
import time
from affaircourse.models import StudentCourse
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
        file_write = open(r'student/error.txt','w')
        file_write.write(e)


def UpdateSelfResult(request, Num):
    # print(Num)
    # print(request.POST)
    TeaName = request.POST.get('Name')
    TeaSex = request.POST.get('Sex')
    TeaCollege = request.POST.get('College')
    TeaMajor = request.POST.get('Major')
    TeaBirth = request.POST.get('Birth')
    # 转换Teabirth的格式
    TeaBirth = time.strptime(TeaBirth, '%Y年%m月%d日')
    TeaBirth = time.strftime('%Y-%m-%d', TeaBirth)
    TeaBirth = datetime.datetime.strptime(TeaBirth, "%Y-%m-%d")
    # print(TeaName)
    # print(TeaSex)
    # print(TeaCollege)
    # print(TeaMajor)
    # print(TeaBirth)
    # print(type(TeaBirth))
    StudentTeacher.objects.filter(TeaNum=Num).update(TeaName=TeaName, TeaSex=TeaSex, TeaCollege=TeaCollege, TeaMajor=TeaMajor, TeaBirth=TeaBirth)
    teacher = StudentTeacher.objects.filter(TeaNum=Num)
    teainfo = teacher[0]

    return render(request, 'teacher/UpdateSelf_Result.html', {"teainfo":teainfo})


def AddCourse(request, Num):
    try:
        teacher = StudentTeacher.objects.filter(TeaNum=Num)
        teainfo = teacher[0]
        return render(request, 'teacher/Course_add.html',{"teainfo": teainfo})
    except Exception as e:
        file_write = open(r'student/error.txt','w')
        file_write.write(e)


def AddCourseResult(request, Num):
    try:
        CourName = request.POST.get('Name')
        CourCredit = request.POST.get('Credit')
        CourPlace = request.POST.get('Place')
        CourType = request.POST.get('Type')
        CourReq = request.POST.get('Require')
        CourTea = request.POST.get('Teacher')
        CourNum = request.POST.get('Num')
        course = StudentCourse()
        course.CourName = CourName
        course.CourCredit = float(CourCredit)
        course.CourPlace = CourPlace
        course.CourType = CourType
        course.CourReq = CourReq
        course.CourTea = CourTea
        course.CourNum = int(CourNum)
        course.save()
        teacher = StudentTeacher.objects.filter(TeaNum=Num)
        teainfo = teacher[0]
        return render(request, 'teacher/Courseadd_result.html', {"teainfo":teainfo})
    except Exception as e:
        file_write = open(r'student/error.txt','w')
        file_write.write(e)
