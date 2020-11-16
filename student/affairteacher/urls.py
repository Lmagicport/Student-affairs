from os import name
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^teacher/lookself/(\d+)$', views.LookSelf, name='lookself'),
    url(r'^teacher/updateself/(\d+)$', views.UpdateSelf, name='updateself')
]
