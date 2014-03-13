from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'chicago_api.views.home', name='home'),
    url(r'^gmap/', include('gmap.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^social_data/',include('social_data.urls')),
)
