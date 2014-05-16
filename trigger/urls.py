from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from control import views

urlpatterns = patterns('',
   url(r'^$', views.ratesmonitor, name='index'),
   url(r'^newrun', views.newrun, name='newrun'),
   url(r'^stoprun', views.stoprun, name='stoprun'),
   url(r'^help', TemplateView.as_view(template_name='control/help.html')),
#   url(r'^$', TemplateView.as_view(template_name='control/index.html')),
   #    url(r'^$', TemplateView.as_view(template_name='runMonitor/index.html')),

)

urlpatterns += staticfiles_urlpatterns()