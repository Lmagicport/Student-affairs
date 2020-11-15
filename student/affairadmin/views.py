from django.shortcuts import render

# Create your views here.
from student.affaircourse.models import StudentCourse


def AdminCourse(request):
  data = StudentCourse.objects.all()
  content = {'data': data}
  return  render(request, 'AdminCourse.html',content)