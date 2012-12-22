#!/usr/bin/python
# -*- coding: UTF-8 -*-

#This file contains spanish-language-specific functionality

#some basic parser settings:

SENTENCE_STOP_TAG           = "Fp"
END_OF_ARTICLE              = "ENDOFARTICLE endofarticle NP00000 0"

##########################################################
# <document end detectors>
##########################################################

def isSeeAlso(words):
    if 4 == len(words):
        return (    u"vea"       == words[0].token.lower() and
                    u"se"        == words[1].token.lower() and
                    u"también"   == words[2].token.lower() and
                    SENTENCE_STOP_TAG == words[3].tag
               )
    else:
        return False 
def isExternalLinks(words):
    if 3 == len(words):
        return  (   u"enlaces"   == words[0].token.lower() and 
                    u"externos"  == words[1].token.lower() and 
                    SENTENCE_STOP_TAG == words[2].tag
                )
    else:
        return False

def isReferences(words):
    if 2 == len(words):
        return (    u"referencias"   == words[0].token.lower() and
                    SENTENCE_STOP_TAG == words[1].tag
               )
    else:
        return False
##########################################################
# </document end detectors>
##########################################################

##########################################################
# <general-purpose Spanish verb functionality>
# This section does not have dependencies on this project
##########################################################

verbEndings={
    'indicative': {
        'present' : {
            'ar' : {
                'firstPerson' : {
                    'singular' : 'o',
                    'plural' :  'amos'
                },
                'secondPerson' : {
                    'singular' : 'as',
                    'plural'   : u'aís'
                },
                'thirdPerson' : {
                    'singular': 'a',
                    'plural'  : 'an'
                }
            },
            'er' : {
                'firstPerson' : {
                    'singular' : 'o',
                    'plural' :  'emos'
                },
                'secondPerson' : {
                    'singular' : 'es',
                    'plural'   : u'eís'
                },
                'thirdPerson' : {
                    'singular': 'e',
                    'plural'  : 'en'
                }
            },
            'ir' : {
                'firstPerson' : {
                    'singular' : 'o',
                    'plural' :  'emos'
                },
                'secondPerson' : {
                    'singular' : 'es',
                    'plural'   : u'eís'
                },
                'thirdPerson' : {
                    'singular': 'e',
                    'plural'  : 'en'
                }
            }
        },#</present>
        'preterite' : {
            'ar' : {
                'firstPerson' : {
                    'singular' : u'é',
                    'plural' :  'amos'
                },
                'secondPerson' : {
                    'singular' : 'aste',
                    'plural'   : 'asteis'
                },
                'thirdPerson' : {
                    'singular': u'ó',
                    'plural'  : 'aron'
                }
            },
            'er' : {
                'firstPerson' : {
                    'singular' : u'í',
                    'plural' :  'imos'
                },
                'secondPerson' : {
                    'singular' : 'iste',
                    'plural'   : u'isteis'
                },
                'thirdPerson' : {
                    'singular': u'ió',
                    'plural'  : 'ieron'
                }
            },
            'ir' : {
                'firstPerson' : {
                    'singular' : u'í',
                    'plural' :  'imos'
                },
                'secondPerson' : {
                    'singular' : 'iste',
                    'plural'   : u'isteis'
                },
                'thirdPerson' : {
                    'singular': u'ió',
                    'plural'  : 'ieron'
                }
            }
        },#</preterite>
        'imperfect' : {
            'ar' : {
                'firstPerson' : {
                    'singular' : 'aba',
                    'plural' :  u'ábamos'
                },
                'secondPerson' : {
                    'singular' : 'abas',
                    'plural'   : 'abais'
                },
                'thirdPerson' : {
                    'singular': u'aba',
                    'plural'  : 'an'
                }
            },
            'er' : {
                'firstPerson' : {
                    'singular' : u'ía',
                    'plural' :   u'íamos'
                },
                'secondPerson' : {
                    'singular' : u'ías',
                    'plural'   : u'íais'
                },
                'thirdPerson' : {
                    'singular': u'ía',
                    'plural'  : u'ían'
                }
            },
            'ir' : {
                'firstPerson' : {
                    'singular' : u'ía',
                    'plural' :   u'íamos'
                },
                'secondPerson' : {
                    'singular' : u'ías',
                    'plural'   : u'íais'
                },
                'thirdPerson' : {
                    'singular': u'ía',
                    'plural'  : u'ían'
                }
            }
        },#</imperfect>
        'future' : {
            'ar' : {
                'firstPerson' : {
                    'singular' : u'aré',
                    'plural' :  u'aremos'
                },
                'secondPerson' : {
                    'singular' : u'arás',
                    'plural'   : u'aréis'
                },
                'thirdPerson' : {
                    'singular': u'ará',
                    'plural'  : u'arán'
                }
            },
            'er' : {
                'firstPerson' : {
                    'singular' : u'eré',
                    'plural' :  u'eremos'
                },
                'secondPerson' : {
                    'singular' : u'erás',
                    'plural'   : u'eréis'
                },
                'thirdPerson' : {
                    'singular': u'erá',
                    'plural'  : u'erán'
                }
            },
            'ir' : {
                'firstPerson' : {
                    'singular' : u'iré',
                    'plural' :  u'iremos'
                },
                'secondPerson' : {
                    'singular' : u'irás',
                    'plural'   : u'iréis'
                },
                'thirdPerson' : {
                    'singular': u'irá',
                    'plural'  : u'irán'
                }
            }
        },#</future>
        'conditional' : {
            'ar' : {
                'firstPerson' : {
                    'singular' : u'aría',
                    'plural' :  u'aríamos'
                },
                'secondPerson' : {
                    'singular' : u'arías',
                    'plural'   : u'aríais'
                },
                'thirdPerson' : {
                    'singular': u'aría',
                    'plural'  : u'arían'
                }
            },
            'er' : {
                'firstPerson' : {
                    'singular' : u'ería',
                    'plural' :  u'eríamos'
                },
                'secondPerson' : {
                    'singular' : u'erías',
                    'plural'   : u'eríais'
                },
                'thirdPerson' : {
                    'singular': u'ería',
                    'plural'  : u'erían'
                }
            },
            'ir' : {
                'firstPerson' : {
                    'singular' : u'iría',
                    'plural' :  u'iríamos'
                },
                'secondPerson' : {
                    'singular' : u'irías',
                    'plural'   : u'iríais'
                },
                'thirdPerson' : {
                    'singular': u'iría',
                    'plural'  : u'irían'
                }
            }
        }#</conditional>
    },#</indicative
    'subjunctive' : {
        'present' : {
             'ar' : {
                'firstPerson' : {
                    'singular' : u'e',
                    'plural' :  u'emos'
                },
                'secondPerson' : {
                    'singular' : u'es',
                    'plural'   : u'éis'
                },
                'thirdPerson' : {
                    'singular': u'e',
                    'plural'  : u'en'
                }
            },
            'er' : {
                'firstPerson' : {
                    'singular' : u'a',
                    'plural' :  u'amos'
                },
                'secondPerson' : {
                    'singular' : u'as',
                    'plural'   : u'áis'
                },
                'thirdPerson' : {
                    'singular': u'a',
                    'plural'  : u'an'
                }
            },
            'ir' : {
                'firstPerson' : {
                    'singular' : u'a',
                    'plural' :  u'amos'
                },
                'secondPerson' : {
                    'singular' : u'as',
                    'plural'   : u'áis'
                },
                'thirdPerson' : {
                    'singular': u'a',
                    'plural'  : u'an'
                }
            }
        },#</present>
        'imperfect' : {
             'ar' : {
                'firstPerson' : {
                    'singular' : (u'ara',u'ase'),
                    'plural' :  (u'áramos', u'ásemos')
                },
                'secondPerson' : {
                    'singular' : (u'aras', u'ases'),
                    'plural'   : (u'arais', u'aseis')
                },
                'thirdPerson' : {
                    'singular': (u'ara',u'ase'),
                    'plural'  : (u'aran',u'asen')
                }
            },
            'er' : {
                'firstPerson' : {
                    'singular' : (u'iera', u'iese'),
                    'plural' :  (u'iéramos', u'iésemos')
                },
                'secondPerson' : {
                    'singular' : (u'ieras', u'ieses'),
                    'plural'   : (u'ierais', u'ieseis')
                },
                'thirdPerson' : {
                    'singular': (u'iera', u'iese'),
                    'plural'  : (u'ieran', u'iesen')
                }
            },
            'ir' : {
                'firstPerson' : {
                    'singular' : (u'iera', u'iese'),
                    'plural' :  (u'iéramos', u'iésemos')
                },
                'secondPerson' : {
                    'singular' : (u'ieras', u'ieses'),
                    'plural'   : (u'ierais', u'ieseis')
                },
                'thirdPerson' : {
                    'singular': (u'iera', u'iese'),
                    'plural'  : (u'ieran', u'iesen')
                }
            }
        }#</imperfect>
    },#</subjunctive>
    'imperative': {
        'ar' : {
            'firstPerson' : {
                'plural' :  'emos'
            },
            'secondPerson' : {
                'singular' : 'a',
                'plural'   : 'ad'
            },
            'thirdPerson' : {
                'singular': 'e',
                'plural'  : 'en'
            }
        },
        'er' : {
            'firstPerson' : {
                'plural' :  'amos'
            },
            'secondPerson' : {
                'singular' : 'e',
                'plural'   : 'ed'
            },
            'thirdPerson' : {
                'singular': 'a',
                'plural'  : 'an'
            }
        },
        'ir' : {
            'firstPerson' : {
                'plural' :  'amos'
            },
            'secondPerson' : {
                'singular' : 'e',
                'plural'   : 'id'
            },
            'thirdPerson' : {
                'singular': 'a',
                'plural'  : 'an'
            }
        }
    }
}

#given a string verb lemma, return its string stem, or False if it is not a verb
#
#@example
# getVerbStem('conocer') == 'conoc'
def getVerbStem(lemma):
    originalLemma = lemma
    lemma = lemma.strip()
    lemma = removeReflexiveEnding(lemma)    
            
    if False == getVerbCategory(lemma):
        return False
    else:
        #it could be a legitimate verb
        return lemma[0:len(lemma)-2]

#given a string lemma, checks to see if reflexive.
#If reflexive, returns the lemma without the terminal 'se'
#Else, returns original lemma
def removeReflexiveEnding(lemma):
    ending = lemma[-2:]

    if 'se' == ending:
        #if reflexive, remove 'se'
        return lemma[0:len(lemma)-2]
    
    return lemma

#given a string verb lemma return a string verb category, or False if not a Verb
# possible values: 'AR', 'ER', 'IR', False
def getVerbCategory(lemma):
    lemma = removeReflexiveEnding(lemma)
    
    ending = lemma[-2:]
    if 'ar' != ending and 'er' != ending and 'ir' != ending:
        return False
    else:
        return ending
    
#Given a regular spanish verb and contextual information, conjugate it.
#@returns string conjugated verb, or, if appropriate, a tuple with the valid conjugations
#Does NOT return correct result for irregular verbs.
#
#@param string lemma - a spanish verb in infinitive form
#@param string mood
#   possible values: ['indicative','subjunctive','imperative','gerund','infinitive','participle']
#
#@param string tense
#   possible values: ['present', 'preterite', 'imperfect', 'conditional', 'future']
#
#@param string person
#   possible values: ['firstPerson', 'secondPerson', 'thirdPerson']
#
#@param string plurality
#   possible values: ['singular', 'plural']
#
#@param Boolean formal. If true, gives Ud. or Uds. conjugations. If false, 
#   gives tú or vosotr@s conjugations.
#
#@param integer subjStyle. Only relevant when mood='subjunctive' and 
#   tense='imperfect'
#   possible values: [0, 1, None]
#
#   0 gives just the '-ra' conjugation
#   1 gives just the '-se' conjugation
#   None gives both in a tuple
#
#@param string gender. Only relevant when mood = 'participle'. 
#   possible values: ['masculine', 'feminine', None]
#   None returns both masculine and feminine as a tuple. The other values return
#   just a string.
#
#@param Boolean affirmative. Only relevant when mood = 'imperative'.
#   possible values: [True, False, None]
#   True returns the affirmative command
#   False returns the negative command
#   None returns both in a (affirmative, negative) tuple
#
#@returns mixed
#   - a string conjugated verb
#   - a tuple of string conjugations if any of the following conditions are met:
#           - requested subjunctive mood and imperfect tense with no value 
#             specified for the 'conjStyle' parameter
#           - requested participle mood and no value was specified for the 
#             'gender' parameter
#           - requested imperative mood and no value was specified for the 
#             'affirmative' parameter
#   - False if the supplied lemma is not an infinitive verb or 
#     if the future subjunctive is requested. (Future subjunctive not supported)
#
def regularlyConjugate(lemma, mood, tense='', person='', plurality='', formal=False, subjStyle=None, gender=None, affirmative=None):

    if 'infinitive' == mood:
        return lemma
    else:
        if formal:
            person = 'thirdPerson'

        cat = getVerbCategory(lemma) #ar/er/ir
        verbStem = getVerbStem(lemma)
        if False == verbStem:
            print ('"%s" does not appear to be an infinitive verb' % lemma)
            return False
        if 'indicative' == mood:
            return verbStem + verbEndings[mood][tense][cat][person][plurality]

        if 'subjunctive' == mood:
            if 'imperfect' == tense:
                #imperfect subjunctive lookups always yield a two-element tuple
                ending0, ending1 = verbEndings[mood][tense][cat][person][plurality]
                conj0 = verbStem + ending0
                conj1 = verbStem + ending1

                if 0 == subjStyle:
                    return conj0
                if 0 == subjStyle:
                    return conj1
                else:
                    return (conj0, conj1)
            elif 'present' == tense:
                return  verbStem + verbEndings[mood][tense][cat][person][plurality]
            elif 'future' == tense:
                print "Future subjunctive not supported."
                return False 
            else:
                print ('"%s" is not a valid tense for mood "subjunctive"' % tense)
                return False

        if 'imperative' == mood:
            if 'firstPerson' == person and 'singular' == plurality:
                #This doesn't exist in spanish.
                #The user really wants a tú command:

                person = 'secondPerson'
                plurality = 'singular'

            aff = verbStem + verbEndings[mood][cat][person][plurality]
            
            #negative commands are just present subjunctive
            neg = verbStem + verbEndings['subjunctive']['present'][cat][person][plurality]
            if None == affirmative:
                #return a tuple
                return (aff, neg)
            elif True == affirmative:
                return aff
            elif False == affirmative:
                return neg
            else:
                print ('"%s" is not a valid option. Use true, false, or None' % affirmative)
                return False
        if 'gerund' == mood:
            if 'ar' == cat:
                return verbStem + 'ando'    
            elif 'er' == cat or 'ir' == cat:
                return verbStem + 'iendo'
            else:
                print ("invalid verb category")
                return False
        if 'participle' == mood:
            ending = ''
            if 'ar' == cat:
                ending += 'ad'
            elif 'er' == cat or 'ir' == cat:
                ending += 'id'

            #gender
            if None == gender:
                ending0 = ending + 'o'
                ending1 = ending + 'a' 
            elif 'masculine' == gender:
                ending += 'o'
            elif 'feminine' == gender:
                ending += 'a'
            else:
                print ("invalid gender")
                return False
            if 'singular' == plurality:
                if None == gender:
                    return (verbStem + ending0, verbStem + ending1)
                else:
                    return verbStem + ending
            elif 'plural' == plurality:
                if None == gender:
                    ending0 += 's'
                    ending1 += 's'
                    return (verbStem + ending0, verbStem + ending1)
                else:
                    ending += 's'
                    return verbStem+ending
            else:
               print ('invalid plurality')
               return False

        else:
            print ("invalid mood")
            return False

##########################################################
# </general-purpose Spanish verb functionality>
##########################################################

##########################################################
# <project-specific Verb functionality>
# depends on functions in this file and conj.models.Verb
##########################################################

#Given an instance of Verb, return a regularly-conjugated string according to 
#the Verb's binary mood, tense, person and plurality attributes.
#
#@param conj.models.Verb v
#@returns string conjugated verb
#@note this does NOT correctly conjugate irregular verbs
def regularlyConjugateVerb(v):
    
    #@note At time of writing these verb attribute names correspond exactly
    #   to the dictionary keys in this file. If the names become non-identical, 
    #   convert the following lists of Verb attribute names into dictionaries 
    #   mapping Verb attribute names to the corresponding dictionary keys in 
    #   this file.
    
    moodAttributeNames = ['indicative','subjunctive','imperative','gerund','infinitive','participle']
    tenseAttributeNames = ['present', 'preterite', 'imperfect', 'conditional', 'future']
    personAttributeNames = ['firstPerson', 'secondPerson', 'thirdPerson']
    pluralityAttributeNames = ['singular', 'plural']
    
    affirmative = v.affirmative
    formal = v.formal

    if v.masculine == None:
        gender = None
    elif(v.masculine):
        gender = 'masculine'
    elif False == v.masculine:
        gender = 'feminine'

    mood = getFirstTrueAttribName(v, moodAttributeNames)
    tense = getFirstTrueAttribName(v, tenseAttributeNames)
    person = getFirstTrueAttribName(v, personAttributeNames)
    plurality = getFirstTrueAttribName(v, pluralityAttributeNames)
    lemma = v.lemma
    
    return regularlyConjugate(lemma, mood, tense, person, plurality, formal, gender=gender, affirmative=affirmative)

#@param object to check
#@param Names of attributes to check on object. This is a subset of properties
#       of the object
#@param Value to compare against
#returns The name of the attribute in object that equalled
def getFirstAttribNameEqualTo(obj, attributeNames, value):
    for attributeName in attributeNames:
        if value == getattr(obj, attributeName):
            return attributeName
            #@note
            # if attribute lists are converted to dictionaries, use this instead
            # return attributeNames[attributeName]
    return None
def getFirstTrueAttribName(obj, attributeNames):
    return getFirstAttribNameEqualTo(obj, attributeNames, True)

##########################################################
# </project-specific Verb functionality>
##########################################################
