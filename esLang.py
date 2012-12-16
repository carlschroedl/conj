#spanish-language-specific:

SENTENCE_STOP_TAG           = "Fp"
END_OF_ARTICLE              = "ENDOFARTICLE endofarticle NP00000 0"

def isSeeAlso(words):
    if 4 == len(words):
        return (    "vea"       == words[0].token.lower() and
                    "se"        == words[1].token.lower() and
                    "tambien"   == words[2].token.lower() and
                    SENTENCE_STOP_TAG == words[3].tag
               )
    else:
        return False 
def isExternalLinks(words):
    if 3 == len(words):
        return  (   "enlaces"   == words[0].token.lower() and 
                    "externos"  == words[1].token.lower() and 
                    SENTENCE_STOP_TAG == words[2].tag
                )
    else:
        return False

def isReferences(words):
    if 2 == len(words):
        return (    "referencias"   == words[0].token.lower() and
                    SENTENCE_STOP_TAG == words[1].tag
               )
    else:
        return False
