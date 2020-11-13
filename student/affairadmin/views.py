from django.shortcuts import render

# Create your views here.
def AdminCourse(request):
  print("111")

  return  render(request, 'AdminCourse.html')