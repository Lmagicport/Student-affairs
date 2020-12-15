from os import name
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^admin/AdminTeacherAdd/$', views.AdminTeacherAdd, name="AdminTeacherAdd"),
    url(r'^admin/AdminStudentAdd/$', views.AdminStudentAdd, name="AdminStudentAdd"),
    url(r'^admin/AdminAddStudent/$', views.AdminAddStudent, name="AdminAddStudent"),
    url(r'^admin/AdminAddTeacher/$', views.AdminAddTeacher, name="AdminAddTeacher"),
    url(r'^admin/search_student/(?P<student_StuNum>[0-9]*)/$', views.search_student, name="search_student"),
#     url(r'^admin/updateStudent/', views.updateStudent),
#     url(r'^admin/search_teacher/(?P<teacher_TeaNum>[0-9]*)/$', views.search_teacher),
#     url(r'^admin/pass/(?P<course_id>[0-9]*)/$', views.pass_course),
#     url(r'^admin/updateTeacher/', views.updateTeacher),
 ]