class Verb:
    id = None
    token = None
    lemma = None
    rawTag = None
    #moods
    indicative = False
    subjunctive = False
    imperative = False
    gerund = False
    infinitive = False
    perfect = False

    #tenses
    present = False
    preterite = False
    imperfect = False
    conditional = False
    #pattern
    irregular = False
    
    #@todo not sure if the following actually can/should be represented in 
    #the data model

    #meta-tense
    #preteriteOrImperfect = None #true if decision between the two tenses
    #meta-mood
    #indicativeOrSubjunctive = None
