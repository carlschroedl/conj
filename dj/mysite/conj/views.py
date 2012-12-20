from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson

from conj.models import *

# just render the template
def index(request):
    return render_to_response('index.html')

# view for ajax requests
def exercise(request):
	if request.is_ajax():
		if request.method == 'GET':
			# get data from database
			exercise = Exercise.objects.get(id=1)
			sentenceObj = exercise.sentence
			sentence = sentenceObj.text
			verb = exercise.verb
			verbLocation = exercise.verbLocation
			# put data in a dictionary
			exerciseData = {'sentence': str(sentence), 'verb': str(verb), 'lemma' : str(verb.lemma)}
			# dump the data into json
			message = simplejson.dumps(exerciseData)
	return HttpResponse(message)