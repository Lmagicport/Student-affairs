from django.db import models
from django.shortcuts import render
from affairteacher.models import StudentTeacher
import datetime
import time
from affaircourse.models import StudentCourse
from affairstudent.models import StudentStudent

def AdminTeacherAdd(request):
  return  render(request, 'AdminTeacherAdd.html')

def AdminStudentAdd(request):
  return  render(request, 'AdminStudentAdd.html')

def AdminCourse(request):
  data = StudentCourse.objects.all()
  content = {'data': data}
  return  render(request, 'AdminCourse.html',content)

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

def search_student(request, student_StuNum):
    student = StudentStudent.objects.filter(StuNum=student_StuNum)
    content = {'data': student}
    print(content)
    return  render(request, 'AdminStudentUpdate.html', content)

def AdminAddTeacher(request):
    print('emmmmmm')
    studentTeacher = StudentTeacher()
    studentTeacher.TeaNum = request.POST['TeaNum']
    studentTeacher.TeaName = request.POST['TeaName']
    studentTeacher.TeaMajor = request.POST['TeaMajor']
    studentTeacher.TeaSex = request.POST['TeaSex']
    studentTeacher.TeaCollege = request.POST['TeaCollege']
    studentTeacher.TeaPass = request.POST['TeaNum']
    studentTeacher.TeaBirth = request.POST['TeaBirth']
    print(studentTeacher.TeaNum)
    studentTeacher.save()
    data = StudentTeacher.objects.all()
    print(data)
    content = {'data': data}
    return render(request, 'AdminTeacher.html',content)
