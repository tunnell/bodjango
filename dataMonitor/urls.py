from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^dash', TemplateView.as_view(template_name='dash.html')),
    url(r'^runs/',include('runMonitor.urls')),
    url(r'^log/',include('log.urls')),
    # url(r'^$', 'dataMonitor.views.home', name='home'),
    # url(r'^dataMonitor/', include('dataMonitor.foo.urls')),
    url(r'^about/',TemplateView.as_view(template_name='about.html')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^control/',include('control.urls')),
    url(r'^trigger/',include('trigger.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
