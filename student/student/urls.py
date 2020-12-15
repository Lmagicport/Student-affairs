"""student URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from student import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^$', views.login),
    url(r'^loginin/$', views.loginin),
    url(r'^loginin/AdminCourse/$', views.AdminCourse),
    url(r'^loginin/AdminStudent/$', views.AdminStudent),
    url(r'^loginin/AdminTeacher/$', views.AdminTeacher),
    # url(r'^AdminCourseAdd/$', views.AdminCourseAdd),
    # url(r'^AdminTeacherAdd/$', views.AdminTeacherAdd),
    # url(r'^AdminStudentAdd/$', views.AdminStudentAdd),
    # url(r'^AdminAddCourse/', views.AdminAddCourse),
    # url(r'^delete/(?P<course_id>[0-9]*)/$', views.delete_course),
    # url(r'^AdminAddStudent/', views.AdminAddStudent),
    # url(r'^AdminAddTeacher/', views.AdminAddTeacher),
    # url(r'^search_student/(?P<student_StuNum>[0-9]*)/$', views.search_student),
    # url(r'^updateStudent/', views.updateStudent),
    # url(r'^search_teacher/(?P<teacher_TeaNum>[0-9]*)/$', views.search_teacher),
    # url(r'^pass/(?P<course_id>[0-9]*)/$', views.pass_course),
    # url(r'^updateTeacher/', views.updateTeacher),
    url(r'^teacher/', include(('affairteacher.urls', 'teacher'), namespace='teacher')),
    url(r'^admin/', include(('affairadmin.urls', 'admin'), namespace='admin')),
]
