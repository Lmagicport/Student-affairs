from os import name
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^teacher/lookself/(\d+)$', views.LookSelf, name='lookself'),
    url(r'^teacher/updateself/(\d+)$', views.UpdateSelf, name='updateself'),
    url(r'^teacher/updateself/result/(\d+)$', views.UpdateSelfResult, name='updateselfresult'),
    url(r'^teacher/addcourse/(\d+)$', views.AddCourse, name='addcourse'),
    url(r'^teacher/addcourse/result/(\d+)$', views.AddCourseResult, name='addcourseresult'),
    url(r'^teacher/lookcourse/(\d+)$', views.LookCourse, name='lookcourse'),
    url(r'^teacher/altercourse/(\d+)$', views.AlterCourse, name='altercourse'),
    url(r'^teacher/altercourse/result/(\d+)$', views.AlterCourseResult, name='altercourseresult'),
    url(r'^teacher/deletecourse/(\d+)$', views.DeleteCourse, name='deletecourse'),
    url(r'^teacher/deletecourse/result/(\d+)$', views.DeleteCourseResult, name='deletecourseresult'),
    url(r'^teacher/addcoursegrade/choose/(\d+)$', views.AddCourseChoose, name='addcoursegradechoose'),
    url(r'^teacher/addcoursegrade/update/(\d+)$', views.AddCourseGrade, name='addcoursegrade'),
    url(r'^teacher/addcoursegrade/result/(\d+)$', views.AddCourseGradeResult, name='addcoursegraderesult')
]
