from trigger.models import TriggerrateInfo
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponsePermanentRedirect
import datetime
from chartit import DataPool, Chart
# Create your views here.

def ratesmonitor(request):
    
    rundata = DataPool(
            series = [{'options': {'source' : TriggerrateInfo.objects.order_by('-createdAt')[:250]},
                       'terms' : ['ratetoss','time','rateout']}
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
                       'time' : ['ratetoss', 'rateout']}
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
    #status = DAQStatus.objects.latest('createdAt')
    return render_to_response('trigger/index.html',{'ratesmonitor_chart': cht},context_instance=RequestContext(request))
