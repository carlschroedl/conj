from django.core.management.base import BaseCommand, CommandError
import sys, django
import xml.etree.ElementTree as ET
import codecs, pprint, cPickle
from inspect import getmembers
from conj.models import *
import fileinput


#create alias
#pp = pprint.pprint
def pp(thing):
    0 == 0
    #turned off for now
    #pprint.pprint(getmembers(thing))

#import parser configuration
import _pcfg as pcfg

#import language-specific module
import _esLang as lang
#@todo: ^make this hot-swappable at runtime

#our classes
from _Word import Word
#from Document import Document
#from Exercise import Exercise
#from Verb import Verb
#from Sentence import Sentence

class Command(BaseCommand):
    args = "<filename>"
    help = 'Parses wikicorpus files and inserts them into the database'
    #<parse helper functions>
    
    def preprocess(self, filename):
        for line in fileinput.input(filename, inplace=True):
            if '&' in line:
                line = line.replace('&', 'y')
            if (line[0] == '<' and line[:4] == '<doc'):
                # if there's more than 10 quotation marks, there are extra in the title
                if line.count('"') > 10:
                    # get the beginning index of the title
                    begin = line.find('title=') + 7
                    # get the ending index of the title
                    end = line.find('nonfiltered=') - 2
                    # split the string into beginning, middle and end
                    b = line[:begin]
                    m = line[begin:end]
                    e = line[end:]
                    
                    # remove the quotes from the title string
                    m = m.replace('"', '')
                    
                    # reconstruct the new string
                    line = b + m + e
                    
                print line,
            elif (line[0] == '<' and line[:6] == '</doc>'):
                 print line,
            elif (line[0] == '<' and line[:4] != '<doc') and (line[0] == '<' and line[:6] != '</doc>'):
                 print '<![CDATA[' + line[:-1] + ']]>\n',
            elif line[0] == '>':
                 print '<![CDATA[' + line[:-1] + ']]>\n',
            else:
                 print line,
    
    #@param words : a list of Word objects comprising a sentence
    #@returns boolean - true if the sentence matches criteria to skip the rest
    #                    of the document like "See Also", "External Links", etc.
    #                   false if it is a normal body-style sentence
    def sentenceSignalsEndOfDoc(self, words):
        return (    lang.isSeeAlso(words) or 
                    lang.isExternalLinks(words) or 
                    lang.isReferences(words)
                )
    
    #Boolean true/false if it is parseable
    def parseable(self, line):
        if pcfg.FIELDS_PER_LINE == len(line.split()):
            return True
        else:
            return False
    
    #returns a tuple of the tokenized line
    def parseLine(self, line):
    #very simple for now
        return line.split()
    
    #given a wikicorpus FreeLing-style POS tag, update verb's boolean features accordingly
    #returns the updated verb
    #@url http://nlp.lsi.upc.edu/freeling/doc/tagsets/tagset-es.html#verbos
    def getTaggedVerb(self, tag, verb):
        #maps the character at tag pos '2' to the property to set true in 'verb' 
        twoMap = {  'S' : 'subjunctive',
                    'I' : 'indicative',
                    'G' : 'gerund',
                    'N' : 'infinitive',
                    'P' : 'participle',
                    'M' : 'imperative'
        }
        attribToSet = twoMap.get(tag[2], False)
        if False == attribToSet:
            print 'error parsing tag:', tag
        else:
            setattr(verb, attribToSet, True)
        
        #maps the character at tag pos '3' to the property to set true in 'verb' 
        threeMap = {    'P' : 'present',
                        'C' : 'conditional',
                        'S' : 'preterite',
                        'I' : 'imperfect',
                        'F' : 'future'
        }
         
        attribToSet = threeMap.get(tag[3], False)
        if False != attribToSet:
            setattr(verb, attribToSet, True)

        fourMap = {
                    '1' : 'firstPerson',
                    '2' : 'secondPerson',
                    '3' : 'thirdPerson'
        }
        
        attribToSet = fourMap.get(tag[4], False)
        if False != attribToSet:
            setattr(verb, attribToSet, True)
   
        fiveMap = {
                    'S' : 'singular',
                    'P' : 'plural'
        }

        attribToSet = fiveMap.get(tag[5], False)
        if False != attribToSet:
            setattr(verb, attribToSet, True)
        
        verb.masculine = ('M' == tag[6])
        
        return verb
    #conjugates the verb lemma for the given context as though it were a 
    #regular verb. Compares the regularly-conjugated result to the actual token
    #the verb's actual token
    def isRegular(self, verb):
        actual = verb.token.lower()
        if hasattr(lang, 'regularlyConjugateVerb'):
            conjugated = lang.regularlyConjugateVerb(verb)
            
            #first check tuple results
            #if ( (verb.subjunctive and verb.imperfect) or 
            #      verb.participle or
            #      verb.imperative):
            
            #first check tuple results
            if isinstance(conjugated, tuple):
                return actual == conjugated[0] or actual == conjugated[1]
            else:
                #if result was not a tuple
                return actual == conjugated
        else:
            print "no regular conjugation functionality available"
            return False

    #</parse helper functions>
    
    #<correct missing root node>
    def handle(self, *args, **options): 
#        #######################################
#        # <testing for regularlyConjugateVerb>
#        ######################################
#        vb = Verb()
#
#        vb.lemma = 'compartir'
#        #mood
#        vb.participle = True
#        #tense
#        vb.present = False
#        #person
#        vb.secondPerson = True
#        #plurality
#        vb.plural = True
#        #affirmitave
#        vb.affirmative = False
#        #gender
#        vb.masculine = True
#
#        print lang.regularlyConjugateVerb(vb)
#        exit()
#        ##################################
#        # </testing>
#        ##################################
        if 0 == len(args):
            print "No file name specified"
            return
        if 0 < len(args):
            filename = args[0]
        if 2 == len(args):
            freqDictFile = open(args[1])
            freqDict = cPickle.load(freqDictFile)
        else:
            freqDict = {}
        self.preprocess(filename)
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
        numDocs = len(docs)
        curDocNum = 0
        for doc in docs:
            curDocNum += 1
            self.stdout.write('Working on Document #%d of %d\n' % (curDocNum, numDocs))
            #setup doc object
            d = Document()
            d.parseId = doc.get('id', None)
            d.title = doc.get('title', None)
            d.nonfiltered = doc.get('nonfiltered', None)
            d.processed = doc.get('processed', None)
            d.dbindex = doc.get('dbindex', None)
            d.save() 
            pp(d)
            #@todo: flush to db
        
            words = []
            for line in doc.text.split("\n"):
                line = line.strip()
                
                #sentence endings are marked by empty lines 
                if len(line) == 0: # if this is the end of the sentence
                    if self.sentenceSignalsEndOfDoc(words):
                        break
                    elif len(words) >=  pcfg.MINIMUM_SENTENCE_LENGTH :
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
                        s.save() 
                        pp(s) 
                        #@todo flush sentence to db
        
                        #now construct various exercises for each verb in the sentence
        
                        exercises = []
                        for indexVerb in verbs: #for each (index, verb) tuple
                            #split the tuple
                            index = indexVerb[0]
                            verbWord = indexVerb[1]
                            
                            #make the Verb object
                            v = Verb()
                            v.token = verbWord.token
                            v.lemma = verbWord.lemma
                            v.rawTag = verbWord.tag
                            if v.lemma in freqDict:
                                v.frequent = True
                            v = self.getTaggedVerb(verbWord.tag, v)
                            v.irregular = not self.isRegular(v) 
                            v.save() 
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
                            exercise.save()
                            pp(exercise)
                            #@todo flush to db
                    #whether or not the minimum length requirement was satisfied,
                    #clear the list of words so that the next sentence can be detected
                    words = []
        
                else: #if this is not the end of a sentence, parse this line
                             
                    if line == lang.END_OF_ARTICLE :
                        break #stop parsing this doc if END_OF_ARTICLE token found
                    else:           
                        if not self.parseable(line):
                            print "The following line was not parseable:"
                            print line
                            print "Skipping document with ID =",doc.attrib['id']
                            break
                        else: 
                            #no errors, time to actually parse:
                            tup = self.parseLine(line)
                            #token, lemma, tag, sense = tup
                            w = Word(*tup)
                            words.append(w)
    
        #</parse the valid xml doc>
