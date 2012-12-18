from django.http import HttpResponse
from django.shortcuts import render_to_response
from conj.models import *

def createInput(lemma):
	return ('<span class="sentence verb"><input type="text" id="verb" /><label for="verb">%s</label></span>') % lemma

def index(request):
    exercise = Exercise.objects.get(id=1)
    sentenceObj = exercise.sentence
    sentence = sentenceObj.text
    verb = exercise.verb
    verbPosition = exercise.verbPosition
    output = ''
    for i, word in enumerate(sentence.split()):
    	if (i == verbPosition):
    		output += createInput(verb.lemma)
    	else:
    		output += word + ' '
    output += verb.token
    return render_to_response('index.html', {'sentence': output})

def exercise(request):
    return HttpResponse("Hello, world. You're trying to access a specific exercise")