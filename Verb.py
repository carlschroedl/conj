class Verb:
    id = None
    token = None
    lemma = None
    rawTag = None
    #moods
    indicative = False
    subjunctive = False
    imperative = False
    #tenses
    present = False
    preterite = False
    imperfect = False
    #pattern
    irregular = False
    
    #@todo not sure if the following actually can/should be represented in 
    #the data model

    #meta-tense
    #preteriteOrImperfect = None #true if decision between the two tenses
    #meta-mood
    #indicativeOrSubjunctive = None
