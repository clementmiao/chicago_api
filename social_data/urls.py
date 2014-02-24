from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'social_data.views.home', name='social-home'),
    (r'^icons/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.BASE_DIR + "/social_data/icons"}),
    # url(r'^icons/(.*)','social_data.views.home')
    # url(r'^icons/(?P<meal_id>\d+)/$', '.views.meal', name='diary-meal'),
)

