from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core import serializers
from django.core.context_processors import csrf

from conj.models import *

import codecs

# view for conjugate page
def index(request):
    return render_to_response('conjugate.html')

# view for ajax requests
def exercise(request):
    output = "" # a blank response if request isn't ajax & (GET||POST)
    if request.is_ajax():
        if request.method == 'GET':
            # get random exercise from database            
            exercise = Exercise.objects.order_by('?')[0]
            output = serializers.serialize('json', [exercise], use_natural_keys=True, ensure_ascii=False)

        if request.method == 'POST':
            exercise = Exercise.objects.get(id=request.POST['pk'])

            output = serializers.serialize('json', [exercise], use_natural_keys=True, ensure_ascii=False)
    #the following is the official json content-type:
    #http://stackoverflow.com/questions/477816/the-right-json-content-type
    return HttpResponse(output, content_type='application/json')
    #return HttpResponse(output, content_type='text/plain; charset=ISO-8859-1')
    #return HttpResponse(output, content_type='text/plain; charset=utf-8')
    
# view for about page
def about(request):
    return render_to_response('about.html')
