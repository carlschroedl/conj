from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core import serializers

from conj.models import *

# just render the template
def index(request):
    return render_to_response('index.html')

# view for ajax requests
def exercise(request):
    output = "" # a blank response if request isn't ajax&GET
    if request.is_ajax():
        if request.method == 'GET':
            # get random exercise from database            
            exercise = Exercise.objects.order_by('?')[0]

            output = serializers.serialize('json', [exercise], use_natural_keys=True)
       
    #the following is the official json content-type:
    #http://stackoverflow.com/questions/477816/the-right-json-content-type
    return HttpResponse(output, content_type='application/json')
    #return HttpResponse(output, content_type='text/plain; charset=ISO-8859-1')
    #return HttpResponse(output, content_type='text/plain; charset=utf-8')

