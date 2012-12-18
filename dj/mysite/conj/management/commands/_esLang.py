#!/usr/bin/python
# -*- coding: UTF-8 -*-
#spanish-language-specific:

SENTENCE_STOP_TAG           = "Fp"
END_OF_ARTICLE              = "ENDOFARTICLE endofarticle NP00000 0"

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
