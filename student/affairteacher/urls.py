from os import name
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^teacher/lookself/(\d+)$', views.LookSelf, name='lookself'),
    url(r'^teacher/updateself/(\d+)$', views.UpdateSelf, name='updateself'),
    url(r'^teacher/updateself/result/(\d+)$', views.UpdateSelfResult, name='updateselfresult'),
    url(r'^teacher/addcourse/(\d+)$', views.AddCourse, name='addcourse'),
    url(r'^teacher/addcourse/result/(\d+)$', views.AddCourseResult, name='addcourseresult')
]
