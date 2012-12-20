from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core import serializers
from django.core.context_processors import csrf

from conj.models import *

# view for conjugate page
def index(request):
	return render_to_response('conjugate.html')

# view for ajax requests
def exercise(request):
	if request.is_ajax():
		if request.method == 'GET':
			# get random exercise from database			
			exercise = Exercise.objects.order_by('?')[0]

			output = serializers.serialize('json', [exercise], use_natural_keys=True)
		if request.method == 'POST':
			exercise = Exercise.objects.get(id=request.POST['pk'])

			output = serializers.serialize('json', [exercise], use_natural_keys=True)
	return HttpResponse(output)
	
# view for about page
def about(request):
    return render_to_response('about.html')
