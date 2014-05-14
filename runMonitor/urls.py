from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from runMonitor import views

urlpatterns = patterns('',
#   url(r'^$', TemplateView.as_view(template_name='runMonitor/index.html')),
   url(r'^$', views.index, name='index'),
   url(r'^uptimedata', views.uptimedata, name='uptimedata'),
   #    url(r'^$', TemplateView.as_view(template_name='runMonitor/index.html')),

)

urlpatterns += staticfiles_urlpatterns()