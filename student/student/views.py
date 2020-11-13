from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os
import json
from affairadmin.models import StudentAdmin
from affaircourse.models import StudentCourse

def login(request):
  return  render(request, 'login.html')

def AdminCourseAdd(request):
  return  render(request, 'AdminCourseAdd.html')

def AdminCourseAddStudent(request):
  print('??')
  studentCourse = StudentCourse()
  studentCourse.CourName = request.POST['CourName']
  studentCourse.CourCredit = request.POST['CourCredit']
  studentCourse.CourReq = request.POST['CourReq']
  studentCourse.CourPlace = request.POST['CourPlace']
  studentCourse.CourType = request.POST['CourType']
  studentCourse.CourTea = request.POST['CourTea']
  print(studentCourse)
  studentCourse.save()
  data = StudentCourse.objects.all()
  content = {'data': data}
  return  render(request, 'AdminCourse.html' , content)

def AdminCourse(request):
  data = StudentCourse.objects.all()
  print(data)
  content = {'data': data}
  print(content)
  return  render(request, 'AdminCourse.html',content)


def loginin(request):
  identity = request.POST['identity']
  username = request.POST['username']
  password = request.POST['password']
  print(identity+username+password)
  if(identity == 'admin'):
    ret = StudentAdmin.objects.filter(AdminUser=username,AdminPass=password)
    print(ret)
    if(len(ret) !=0):
      return render(request, 'admin.html')
    else:
      return render(request, 'error.html')
  elif(identity == 'teacher'):
    return render(request, 'teacher.html')
  else:
    return render(request, 'student.html')
  # return render(request, 'teacher.html')
