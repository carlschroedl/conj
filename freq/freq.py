import sys
import os
import codecs
from pprint import pprint

totalVerbs = 0
cumulative = 0

#lang_files = ['corrected_sample']
lang_files = []
for subdir, dirs, files in os.walk('../../tagged.es/'):
	for file in files:
		lang_files.append(file)

def load(filename, dict):
	with codecs.open(filename, 'r', 'ISO-8859-1') as f:
		for line in f:
			words = line.split()
			if len(words) > 3:
				if words[2][0] == 'V':
					dict[words[1]] = dict.get(words[1], 0) + 1
		
# process the pprint-ed intermediate files			
def loadProcessed(filename, dict):
	with codecs.open(filename, 'r', 'ISO-8859-1') as f:
		for line in f:
			words = line.strip().split()
			dict[words[0][2:-2]] = dict.get(words[0][2:-2], 0) + int(words[1][:-1])
			global totalVerbs 
			totalVerbs += 1
			
# modified pprint for testing
def p(sortedList):
	with codecs.open('output.txt', 'w', 'ISO-8859-1') as o:
		for tup in sortedList:
			global totalVerbs
			global cumulative
			percentage = float(tup[1]) / totalVerbs
			cumulative += percentage
			o.write(tup[0] + ' ' + str(percentage) + ' ' + str(cumulative) + '\n')

# process the files and write intermediate output				
for fn in lang_files:
	verbs = {}
	load('../../tagged.es/' + fn, verbs)
	with codecs.open(fn + '_processed', 'w', 'ISO-8859-1') as i:
		pprint(verbs, i)
	
# process the processed files to find overall frequency
verbs = {}
for fn in lang_files:
	loadProcessed(fn + '_processed', verbs)
	
# write out final output
sortedVerbs = sorted(verbs.items(), key=lambda x: x[1])[::-1]
p(sortedVerbs[:1000])
