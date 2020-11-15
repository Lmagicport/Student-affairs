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
from affairteacher.models import StudentTeacher
from affairstudent.models import StudentStudent

def login(request):
  return  render(request, 'login.html')

def AdminCourseAdd(request):
  return  render(request, 'AdminCourseAdd.html')

def AdminStudentAdd(request):
  return  render(request, 'AdminStudentAdd.html')

def AdminTeacherAdd(request):
  return  render(request, 'AdminTeacherAdd.html')

def AdminAddCourse(request):
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
  content = {'data': data}
  return  render(request, 'AdminCourse.html',content)

def delete_course(request, course_id):
  print(course_id)
  StudentCourse.objects.filter(id=course_id).delete()
  data = StudentCourse.objects.all()
  content = {'data': data}
  return render(request, 'AdminCourse.html',content)

def AdminStudent(request):
  data = StudentStudent.objects.all()
  content = {'data': data}
  return  render(request, 'AdminStudent.html',content)


def loginin(request):
  identity = request.POST['identity']
  username = request.POST['username']
  password = request.POST['password']
  print(identity+username+password)
  if(identity == 'admin'):
    ret = StudentAdmin.objects.filter(AdminUser=username, AdminPass=password)
    print(ret)
    if(len(ret) !=0):
      print("??")
      return render(request, 'admin.html')
    else:
      return render(request, 'error.html')
  elif(identity == 'teacher'):
    ret = StudentTeacher.objects.filter(TeaNum=username, TeaPass=password)
    if (len(ret) != 0):
      Name = ret[0].TeaName
      print(Name)
      return render(request, 'teacher.html',{"name":Name})
    else:
      return render(request, 'error.html')
  else:
    ret = StudentStudent.objects.filter(StuNum=username, StuPass=password)
    if (len(ret) != 0):
      return render(request, 'student.html')
    else:
      return render(request, 'error.html')

def AdminAddStudent(request):
    print('??')
    studentStudent = StudentStudent()
    studentStudent.StuNum = request.POST['StuNum']
    studentStudent.StuName = request.POST['StuName']
    studentStudent.StuAge = request.POST['StuAge']
    studentStudent.StuSex = request.POST['StuSex']
    studentStudent.StuCollege = request.POST['StuCollege']
    studentStudent.StuMajor = request.POST['StuMajor']
    studentStudent.StuGra = request.POST['StuGra']
    studentStudent.StuPass = request.POST['StuNum']
    print(studentStudent)
    studentStudent.save()
    data = StudentStudent.objects.all()
    content = {'data': data}
    return render(request, 'AdminStudent.html', content)

def search_student(request,student_StuNum):
    student=StudentStudent.objects.filter(StuNum=student_StuNum)
    content = {'data': student}
    print(content)
    return  render(request, 'AdminStudentUpdate.html', content)

@csrf_exempt
def updateStudent(request):

    StuNum=request.POST['StuNum']
    StuName = request.POST['StuName']
    StuAge = request.POST['StuAge']
    StuSex = request.POST['StuSex']
    StuCollege = request.POST['StuCollege']
    StuMajor = request.POST['StuMajor']
    StuGra = request.POST['StuGra']

    StudentStudent.objects.filter(StuNum=StuNum).update(StuName=StuName,StuAge=StuAge,StuSex=StuSex,StuCollege=StuCollege,StuMajor=StuMajor,StuGra=StuGra)
    data = StudentStudent.objects.all()
    content = {'data': data}
    return render(request, 'AdminStudent.html', content)


def AdminTeacher(request):
  data = StudentTeacher.objects.all()
  content = {'data': data}
  return  render(request, 'AdminTeacher.html',content)


def AdminAddTeacher(request):
    print('emmmmmm')
    studentTeacher = StudentTeacher()
    studentTeacher.TeaNum = request.POST['TeaNum']
    studentTeacher.TeaName = request.POST['TeaName']
    studentTeacher.TeaMajor = request.POST['TeaMajor']
    studentTeacher.TeaSex = request.POST['TeaSex']
    studentTeacher.TeaCollege = request.POST['TeaCollege']
    studentTeacher.TeaPass = request.POST['TeaNum']
    print(studentTeacher)
    studentTeacher.save()
    data = StudentTeacher.objects.all()
    print(data)
    content = {'data': data}
    return render(request, 'AdminTeacher.html',content)


def search_teacher(request,teacher_TeaNum):
    teacher=StudentTeacher.objects.filter(TeaNum=teacher_TeaNum)
    content = {'data': teacher}
    print(content)
    return  render(request, 'AdminTeacherUpdate.html', content)


@csrf_exempt
def updateTeacher(request):

    TeaNum=request.POST['TeaNum']
    TeaName = request.POST['TeaName']
    TeaSex = request.POST['TeaSex']
    TeaCollege = request.POST['TeaCollege']
    TeaMajor = request.POST['TeaMajor']

    StudentTeacher.objects.filter(TeaNum=TeaNum).update(TeaName=TeaName,TeaSex=TeaSex,TeaCollege=TeaCollege,TeaMajor=TeaMajor)
    data = StudentTeacher.objects.all()
    content = {'data': data}
    return render(request, 'AdminTeacher.html', content)