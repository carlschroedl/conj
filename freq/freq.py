import sys
import os
import codecs
from pprint import pprint
import pickle

ENCODING = 'latin_1'

totalVerbs = 0
cumulative = 0

#lang_files = ['corrected_sample']
lang_files = []
for subdir, dirs, files in os.walk('../../tagged.es/'):
	for file in files:
		lang_files.append(file)

def load(filename, dict):
	with codecs.open(filename, 'r', ENCODING) as f:
		for line in f:
			words = line.split()
			if len(words) > 3:
				if words[2][0] == 'V':
					dict[words[1]] = dict.get(words[1], 0) + 1
		
# process the pprint-ed intermediate files			
def loadProcessed(filename, dict):
	# open pickled file
	with open(filename, 'rb') as f:
		# store processed dictionary as intermediate
		intermediate = pickle.load(f)
		# iterate through keys in processed dict and update master dict
		for key in intermediate:
			dict[key] = dict.get(key, 0) + intermediate[key]
			global totalVerbs 
			totalVerbs += 1
			
# modified pprint for testing
def p(sortedList):
	# write human readable list
	pickledList = []
	with codecs.open('output.txt', 'w', ENCODING) as o:
		for index, tup in enumerate(sortedList):
			global totalVerbs
			global cumulative
			percentage = float(tup[1]) / totalVerbs
			cumulative += percentage
			o.write(tup[0] + ' ' + str(percentage) + ' ' + str(cumulative) + '\n')
			pickledList.append((tup[0], index + 1))
	# write pickled version
	with codecs.open('output.pkl', 'wb') as o:
		pickle.dump(pickledList, o)
	
# reads in the pickled output to create a dictionary of most frequent verbs		
def top(fn):
	freqVerbs = {}
	# output.pkl is a sorted list of tuples where first elem is word and 
	# second elem is rank
	with open(fn, 'rb') as i:
		sortedList = pickle.load(i)
		for elem in sortedList:
			freqVerbs[elem[0]] = elem[1]
	return freqVerbs
			

# process the files and write intermediate output				
for fn in lang_files:
	verbs = {}
	load('../../tagged.es/' + fn, verbs)
	with open(fn + '_processed', 'wb') as i:
		# pickle the dictionary into intermediate file
		pickle.dump(verbs, i)

# process the processed files to find overall frequency
verbs = {}
for fn in lang_files:
	loadProcessed(fn + '_processed', verbs)
	
# write out final output
sortedVerbs = sorted(verbs.items(), key=lambda x: x[1])[::-1]
p(sortedVerbs[:1000])

# read back the output.txt to get a dictionary representation
freqVerbs = top('output.pkl')
pprint(freqVerbs)




