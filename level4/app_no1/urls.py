from django.conf.urls import url
from app_no1 import views

#template tagging

app_name = 'app_no1'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),


]
