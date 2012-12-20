from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core import serializers

from conj.models import *

# just render the template
def index(request):
    return render_to_response('index.html')

# view for ajax requests
def exercise(request):
	if request.is_ajax():
		if request.method == 'GET':
			# get random exercise from database			
			exercise = Exercise.objects.order_by('?')[0]

			output = serializers.serialize('json', [exercise], use_natural_keys=True)
	return HttpResponse(output)