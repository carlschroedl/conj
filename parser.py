import sys
import xml.etree.ElementTree as ET
import codecs
import pprint
from inspect import getmembers

#create alias
#pp = pprint.pprint
def pp(thing):
    pprint.pprint(getmembers(thing))

#import parser configuration
import pcfg

#import language-specific module
import esLang as lang
#@todo: ^make this hot-swappable at runtime

#our classes
from Word import Word
from Document import Document
from Exercise import Exercise
from Verb import Verb
from Sentence import Sentence

filename = sys.argv[1]

#<parse helper functions>

#@param words : a list of Word objects comprising a sentence
#@returns boolean - true if the sentence matches criteria to skip the rest
#                    of the document like "See Also", "External Links", etc.
#                   false if it is a normal body-style sentence
def sentenceSignalsEndOfDoc(words):
    return (    lang.isSeeAlso(words) or 
                lang.isExternalLinks(words) or 
                lang.isReferences(words)
            )

#Boolean true/false if it is parseable
def parseable(line):
    if pcfg.FIELDS_PER_LINE == len(line.split()):
        return True
    else:
        return False

#returns a tuple of the tokenized line
def parseLine(line):
#very simple for now
    return line.split()

def parseTag(tag):
    #@todo actually parse the tag
    return (True, True, True, True, True, True, True) 

#</parse helper functions>

#<correct missing root node>

file = codecs.open(filename, 'r', pcfg.ENCODING)
firstline = file.readline().strip()

if firstline != pcfg.ROOT_START_TAG:
    filename = pcfg.CORRECTED_FILENAME_PREFIX + filename
    
    print "No root xml element detected. Correcting and writing to:"
    print filename
    print "..."
    
    newFile = codecs.open(filename, 'w', pcfg.ENCODING)
    newFile.write(pcfg.ROOT_START_TAG + "\n")

    file.seek(0) #rewind to beginning of file
    newFile.write(file.read()) #write old into new
    file.close()
    newFile.write(pcfg.ROOT_END_TAG + "\n")
    newFile.close()

    print "Finished writing to" ,filename, "."
    print filename, "will now be parsed."

#</correct missing root node>

#<parse the valid xml doc>

#for docs on XMLParser
#@see: http://docs.python.org/2/library/xml.etree.elementtree.html#module-xml.etree.ElementTree

parser = ET.XMLParser(encoding=pcfg.ENCODING)
et = ET.parse(filename, parser)
root = et.getroot()
docs = root.findall('doc')
for doc in docs:
    
    #setup doc object
    d = Document()
    d.parseId = doc.get('id', None)
    d.title = doc.get('title', None)
    d.nonfiltered = doc.get('nonfiltered', None)
    d.processed = doc.get('processed', None)
    d.parseDbIndex = doc.get('dbindex', None)
    
    pp(d)
    #@todo: flush to db

    words = []
    for line in doc.text.split("\n"):
        line = line.strip()
        
        #sentence endings are marked by empty lines 
        if len(line) == 0: # if this is the end of the sentence
            if sentenceSignalsEndOfDoc(words):
                break
            else:
                #parse sentence, move into ORM objects, update DB appropriately
                sentenceText = ''
                s = Sentence()
                s.document = d
                verbs = [] #list of (location, word) tuples
                indexWithSpaces = 0 #index into the sentence text, a space-delimited string of tokens
                for i, word in enumerate(words):
                    if 'V' == word.tag[0]: #if verb
                        verbs.append((indexWithSpaces, word))
                    #verb, or not:
                    if 0 != i: #if beginning of sentence don't prepend space, else, do.
                        sentenceText += " "
                    
                    indexWithSpaces += len(word.token) + 1 # +1 for the space

                    sentenceText += word.token
                    
                s.text = sentenceText
                s.document = d  
                
                pp(s) 
                #@todo flush sentence to db

                #now construct various exercises for each verb in the sentence

                exercises = []
                for indexVerb in verbs:
                    #split the tuple
                    index = indexVerb[0]
                    verbWord = indexVerb[1]
                    
                    #make the Verb object
                    v = Verb()
                    v.token = verbWord.token
                    v.lemma = verbWord.lemma
                    v.rawTag = verbWord.tag

                    ind, subj, imperative, pres, pret, imperfect, irr = parseTag(verbWord.tag)
                    v.indicative = ind
                    v.subjunctive = subj
                    v.imperative = imperative
                    v.present = pres
                    v.preterite = pret
                    v.imperfect = imperfect
                    v.irregular = irr
                    
                    
                    pp(v)
                    #@todo flush v to db
                    
                    #make the Exercise object
                    ex = Exercise()
                    ex.verbLocation = index
                    ex.sentence = s
                    ex.verb = v

                    exercises.append(ex)

                #flush all exercises to db
                for exercise in exercises:
                    pp(exercise)
                    #@todo flush to db

        else: #if this is not the end of a sentence, parse this line
                     
            if line == lang.END_OF_ARTICLE :
                break #stop parsing this doc if END_OF_ARTICLE token found
            else:           
                if not parseable(line):
                    print "The following line was not parseable:"
                    print line
                    print "Skipping document with ID =",doc.attrib['id']
                    break
                else: 
                    #no errors, time to actually parse:
                    tup = parseLine(line)
                    #token, lemma, tag, sense = tup
                    w = Word(*tup)
                    words.append(w)

exit()


#</parse the valid xml doc>
