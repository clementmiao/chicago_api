from django.conf.urls import patterns, url

from gmap import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)