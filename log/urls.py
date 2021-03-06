from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import log.views

urlpatterns = patterns('',
    url(r'^$', log.views.index, name='index'),
    url(r'^newlogentry/$', log.views.newlogentry,name='newlogentry'),
    #    url(r'^$', TemplateView.as_view(template_name='runMonitor/index.html')),

)

urlpatterns += staticfiles_urlpatterns()