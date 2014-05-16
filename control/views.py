from control.models import rateInfo, DAQStatus, DAQCommand, DAQCommandDBEntry
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponsePermanentRedirect
import datetime
from chartit import DataPool, Chart
# Create your views here.

def newrun(request):
    if request.method == 'POST':
        new_run = DAQCommand(request.POST)
        if new_run.is_valid():
            new_entry = DAQCommandDBEntry(command=new_run.cleaned_data['command'],name=new_run.cleaned_data['name'],mode=new_run.cleaned_data['mode'])
            new_entry.save()
        return HttpResponsePermanentRedirect('/control/')
    else:
        new_run = DAQCommand()
    return render(request, 'control/newrun.html',{'form':new_run,})

def stoprun(request):
    if request.method == 'POST':
        stop_run = DAQCommand(request.POST)
        if stop_run.is_valid():
            new_entry = DAQCommandDBEntry(command=stop_run.cleaned_data['command'],name=stop_run.cleaned_data['name'],mode='none')
            new_entry.save()
        return HttpResponsePermanentRedirect('/control/')
    else:
        stop_run = DAQCommand()
    return render(request,'control/stoprun.html',{'form':stop_run,})

def ratesmonitor(request):
    
    rundata = DataPool(
            series = [{'options': {'source' : rateInfo.objects.filter(node='xedaq02').order_by('-createdAt')[:250]},
                       'terms' : ['datarate','timeseconds']}
                    ])
    
    def timestring(timeint):
        return ((datetime.datetime.fromtimestamp(timeint)).strftime('%H:%M'))
    
    cht = Chart(
            datasource = rundata,
            series_options = 
                [{'options': {
                    'type' : 'area',
                    'stacking' : True,
                    'pointPadding' : 0,
                    'borderWidth' : 0,
                    'stack' : 0},
                   'terms': {
                       'timeseconds' : ['datarate']}
                    }],
            chart_options = 
              {'title': { 'text' : 'Data Rate' },
               'credits': { 'enabled' : False },
               'xAxis': { 'title' : {'text': 'time' },
                          'labels' : {'enabled' :True},
                          'tickInterval' : 100 },
                'chart' : {'zoomType' : 'xy'},
               'yAxis': { 'title' : {'text': 'rate (MB/s)'}               
               }},
            x_sortf_mapf_mts = (None, timestring, False))

    #now get DAQ status
    status = DAQStatus.objects.latest('createdAt')
    return render_to_response('control/index.html',{'ratesmonitor_chart': cht, 'currentStatus' : status},context_instance=RequestContext(request))