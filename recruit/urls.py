from django.conf.urls import url, include
#from django.contrib import admin
from . import views

app_name='recruit'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^add/$', views.add_recruit, name='add'),
    url(r'^exist/$', views.exist_recruit, name='exist'),
    url(r'^records/$', views.RecordView.as_view(), name='records'),

]
