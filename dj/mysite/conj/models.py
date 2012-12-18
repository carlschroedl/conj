from django.db import models

# Create your models here.
class Verb(models.Model):
    token = models.CharField(max_length=50)
    lemma = models.CharField(max_length=50)
    rawTag = models.CharField(max_length=10)
    
    def __unicode__(self):
        return self.token
    
class Document(models.Model):
    idNum = models.IntegerField()
    title = models.CharField(max_length=256)
    nonfiltered = models.IntegerField()
    processed = models.IntegerField()
    dbindex = models.IntegerField()
    
    def __unicode__(self):
        return str(self.idNum)
    
class Sentence(models.Model):
    document = models.ForeignKey(Document)
    text = models.TextField()
    
    def __unicode__(self):
        return self.text

class Exercise(models.Model):
    sentence = models.ForeignKey(Sentence)
    verb = models.ForeignKey(Verb)
    verbPosition = models.IntegerField()
    
    def __unicode__(self):
        return str(self.id)