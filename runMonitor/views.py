from django.shortcuts import render_to_response, render, HttpResponse
#from pygooglechart import PieChart3D
#from chartit import DataPool, Chart
from django.template import RequestContext, loader
import json
from runMonitor.models import runInfo
import datetime

def index(request):
    latest_run_list = runInfo.objects.order_by('-starttimestamp')[:100]
    template = loader.get_template('runMonitor/index.html')
    context = RequestContext(request, {
              'latest_run_list':latest_run_list
              })
    return HttpResponse(template.render(context))

def uptimedata(request):
    a = 0
    b = 0
    lasttimestamp = datetime.datetime.now()-datetime.timedelta(days=100000)

    runInfoList = runInfo.objects.order_by('starttimestamp')
    for p in runInfoList:
        if p.endtimestamp != None:
            td = p.endtimestamp - p.starttimestamp
            a+= td.seconds        
            if (datetime.datetime.now() - lasttimestamp).days<50000:
                td = p.starttimestamp-lasttimestamp
                b+= td.seconds
            lasttimestamp = p.endtimestamp
        else:
            td = datetime.datetime.now()-p.starttimestamp
            a+= td.seconds
          
    #params = request.GET #add params later
    #days  params.get('days',0)
    data = dict({'uptime': a, 'downtime': b})
    return HttpResponse(json.dumps(data),content_type='application/json')

            #datadict = dict({'uptime':a, 'downtime':b})
#    rundata = DataPool(
 #           series = [{'options': {'source' : datadict},
  #          'terms' : ['uptime','downtime']}])            
  #  cht = Chart( datasource = rundata,
   #              series_options = [{'options':{ 'type':'pie'},
    #             'terms':{ 'uptime' : ['downtime']}}],
     #            chart_options =
      #           {
       #          'title': {'text':'Uptime'},
        #         }
         #        )
                                                                                   
#    rundata = DataPool(
#            series=
##            [{'options': {'source' : runInfo.objects.all()},
#              'terms' : ['name','starttimestamp','mode']}
#            ])
#    cht = Chart(
#            datasource = rundata,
#            series_options = 
#                 [{'options':{
#                    'type' : 'column',
#                    'stacking' : True},
#                'terms':{
#                    'name' : ['size']
#            }}],
#            chart_options = 
#                {
#                 'title': {'text':'Run sizes'},
#                 'xAxis': {'title': {'text': 'Run Number'}}
#                })

#    return render_to_response('runMonitor/index.html',{'rundatachart':cht})

#def index(request):
#    chart = PieChart3D(250,100)
#    chart.add_data([20,10])
#    chart.set_pie_labels(['Hello', 'World'])
#    context = RequestContext(request, {
#        'url_to_runchart': chart.get_url()
#    })
#    template = 'runMonitor/index.html'
#    return render_to_response(template,context)

# Create your views here.
