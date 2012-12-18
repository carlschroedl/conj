from django.db import models

# Create your models here.
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
    future = models.BooleanField(default=False)
    #tenses
    present = models.BooleanField(default=False)
    preterite = models.BooleanField(default=False)
    imperfect = models.BooleanField(default=False)
    conditional = models.BooleanField(default=False)
    #pattern
    irregular = models.BooleanField(default=False)
    #frequency
    frequent = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.token
    
class Document(models.Model):
    parseId = models.IntegerField()
    title = models.CharField(max_length=256)
    nonfiltered = models.IntegerField()
    processed = models.IntegerField()
    dbindex = models.IntegerField()
    
    def __unicode__(self):
        return str(self.title)
    
class Sentence(models.Model):
    document = models.ForeignKey(Document)
    text = models.TextField()
    
    def __unicode__(self):
        return self.text

class Exercise(models.Model):
    sentence = models.ForeignKey(Sentence)
    verb = models.ForeignKey(Verb)
    verbLocation = models.IntegerField()
    flagCount = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.id)