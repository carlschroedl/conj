from django.db import models
#@note If you change the names of Verb's existing attributes you will need to 
#change dictionary key names in  _esLang.py or create a mapping between the 
#names of the model attributes and the corresponding _esLang.py-specific keys.
class Verb(models.Model):
    token = models.CharField(max_length=50)
    lemma = models.CharField(max_length=50)
    rawTag = models.CharField(max_length=10)
    
    #mood
    indicative = models.BooleanField(default=False)
    subjunctive = models.BooleanField(default=False)
    imperative = models.BooleanField(default=False)
    gerund = models.BooleanField(default=False)
    infinitive = models.BooleanField(default=False)
    participle = models.BooleanField(default=False)
    #tenses
    present = models.BooleanField(default=False)
    preterite = models.BooleanField(default=False)
    imperfect = models.BooleanField(default=False)
    conditional = models.BooleanField(default=False)
    future = models.BooleanField(default=False) 
    #pattern
    irregular = models.BooleanField(default=False)
    #frequency
    frequent = models.BooleanField(default=False)
    #person
    firstPerson = models.BooleanField(default=False)
    secondPerson = models.BooleanField(default=False)
    thirdPerson = models.BooleanField(default=False)
    #plurality
    singular = models.BooleanField(default=False)
    plural = models.BooleanField(default=False)
    
    def natural_key(self):
        return (self.token, self.lemma, self.rawTag, self.indicative, self.subjunctive,
                self.imperative, self.gerund, self.infinitive, self.participle, 
                self.present, self.preterite, self.imperfect, self.conditional,
                self.future, self.irregular, self.frequent, self.firstPerson,
                self.secondPerson, self.thirdPerson, self.singular, self.plural)
        
    def __unicode__(self):
        return self.token
    
class Document(models.Model):
    parseId = models.IntegerField()
    title = models.CharField(max_length=256)
    nonfiltered = models.IntegerField()
    processed = models.IntegerField()
    dbindex = models.IntegerField()
    
    def natural_key(self):
        return (self.parseId, self.title, self.nonfiltered, self.processed, self.dbindex)
    
    def __unicode__(self):
        return str(self.title)
    
class Sentence(models.Model):
    document = models.ForeignKey(Document)
    text = models.TextField()
    
    def natural_key(self):
        return (self.text,) + self.document.natural_key()
    
    def __unicode__(self):
        return self.text

class Exercise(models.Model):
    sentence = models.ForeignKey(Sentence)
    verb = models.ForeignKey(Verb)
    verbLocation = models.IntegerField()
    flagCount = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.id)
