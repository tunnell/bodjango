from trigger.models import TriggerrateInfo
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponsePermanentRedirect
import datetime
from chartit import DataPool, Chart
import pymongo
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

    def get_db_stats(db_name):
        keys, values = [], []

        db = pymongo.Connection()[db_name]
        result = db.command("dbStats")
        
        storageSize_in = result['storageSize']

        keys.append('Size on %s on disk [MB]' % db_name)
        values.append('%d' % (result['storageSize'] / 1024. / 1024.))

        keys.append('Size of %s data [MB]' % db_name)
        values.append('%d' % (result['dataSize'] / 1024. / 1024.))
                   
        for name in db.collection_names():
            name = str(name)
            if not name.startswith('dataset'):
                continue
            if db_name == 'input':
                keys.append('Occurences in %s to be built' % (name))
            else:
                keys.append('Built events in %s' % (name))
            values.append(db[name].count())
        return zip(keys, values)
    
    db_stats = get_db_stats('input') + get_db_stats('output')
    print(db_stats)

    #now get DAQ status
    #status = DAQStatus.objects.latest('createdAt')
    return render_to_response('trigger/index.html',
                              {'ratesmonitor_chart': cht,
                               'db_stats' : db_stats},
                              context_instance=RequestContext(request))
