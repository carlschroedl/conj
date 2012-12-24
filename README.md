#Aprender
-----

#Summary

Class project for CS 545 with [Professor Benjamin Snyder](http://pages.cs.wisc.edu/~bsnyder/) at UW-Madison. Provides an open-source Spanish conjugation driller. Presents user with a sentence from Wikipedia that has an input field in 
place of a verb in the sentence. Information on the missing verb, including 
infinitive and relevant conjugation information, is shown under the input field. 
The user is asked to fill in the correct conjugation and then press *Check 
Answer*. The user will then receive feedback on their answer and if they want to 
they can choose *Get New Exercise* to get a new random sentence from the corpus.

#Features

##User Interface
-----------------
The web interface retrieves verb conjugation exercises from the server via an ajax call when the user clicks the *Get New Exercise* button.

##Wikicorpus Parser
-------------------
The two-pass parser extracts document, sentence, and verb information from wikicorpus files, creates exercises and persists all of the objects to database. This is implemented as a Django command, and as such files relevant to the implementation are located in dj/mysite/conj/management/commands/ .

##Frequency Analysis
------------------
We were able to do some additional preprocessing of the wikicorpus and we were 
able to define the top 1000 most common verbs in the corpus. The human readable 
output of this analysis can be found in /freq/output.txt. We then determined 
that a verb could be defined as 'frequent' if it occurred in more than 1% of 
the corpus. This amounted to 478 verbs (out of over 86,000 total) that are 
stored in a Python dictionary object in the file freq.pkl.

This implementation is found in freq/freq.py .

##Regular Conjugator
------------------
We also implemented a regular spanish verb conjugator that supports all the most commonly-used contexts in the spanish language. Specifically, it supports:

Moods: Indicative, subjunctive, imperative, gerund, participle and the trivial case: infinitive

Tenses: Present, future, preterite, imperfect, conditional

Subjects: yo, tú, él, ella, usted, nosotros, nosotras, vosotros, vosotras, ellos, ellas, ustedes

This implementation is found in dj/mysite/conj/management/commands/_esLang.py .

#Installation
----------------------

##Software Dependencies
-------
- [Python 2.7.3](http://www.python.org/download/releases/2.7.3/)
- [Django 1.4.2](https://www.djangoproject.com/download/1.4.2/tarball/)
More information on installing Django https://docs.djangoproject.com/en/dev/intro/install/
- [jQuery](http://jquery.com/) (already included in this repo)
- [KnockoutJS](http://knockoutjs.com/)(already included in this repo)

##Data Dependencies
-------
- [The Spanish Wikicorpus dataset](http://www.lsi.upc.edu/~nlp/wikicorpus/)


Once the dependencies are installed, clone this repo to a local directory. Place the Wikicorpus data files in the dj/mysite/ directory.

#Use
----------------

##Parsing the Wikicorpus
----------------------
To add additional exercises to your database, you will need to parse Wikicorpus files. The Wikicorpus parser includes a two-step process that preprocesses the Wikicorpus dump files and then parses each document into new database model objects. If you are curious about the server-side data models, look at dj/mysite/conj/models.py.

To use the parser you can run:
```
python manage.py insertWikiCorpus <wikicorpus file> <frequency pickle file>
```
from the dj/mysite/ directory. The last arg will usually be "freqDict.pkl", a symlink provided in this directory for convenience.

##Running the development web server
----------------
Run:
```
python manage.py runserver
```

From the dj/mysite/ directory

##Using the web app
Go to http://localhost:8000 to begin the exercises.

#Configuration
---------

##Database
--------
The default database is SQLite. Since the Django ORM supports many database engines, it is easy to use other database engines. You can customize the database configuration by modifying the settings in dj/mysite/conj/settings.py

More information on custom database configurations is available [here](https://docs.djangoproject.com/en/dev/ref/databases/).

##Parser
-------
The parser configuration is found at dj/mysite/conj/management/commands/_pcfg.py .

##Web Server
---------
The use instructions are for the development web server. In production, this can and should be changed to interact with a real web server. See the [official Django docs](https://docs.djangoproject.com/en/dev/howto/deployment/) for information on configuring Django to work with a production web server

#Potential Extensions of the Features
---------------------------

##Web Interface, Ajax Handler
----------------------

The *Get New Exercise* function currently does an ajax request for a random sentence 
in the database. The view models and ajax handler can easily be extended to allow the client to take full advantage of the information stored in the server-side models and thus request particular categories of exercise.
The server-side models currently categorize verbs by:
- Mood (Subjunctive, indicative, etc.)
- Tense (Present, imperfect, etc.)
- Subject (First person singular, second person plural etc.)
- Regularity (Irregular/Regular)

##Parser
------------

The parser was written in language-independent form. Spanish is currently supported. Additional languages can be supported by implementing the functionality of dj/mysite/management/conj/_esLang.py for a different langauge, and changing the imports in the insertWikiCorpus file to match.

A single-pass parser can be implemented. Start with the assumption that the wikicorpus files do not use valid xml and hence should be purely line-based.

##Regular Conjugator
------------------
The regular conjugator can easily be extended to support the uncommon future subjunctive tense and the rioplatense-specific pronoun 'vos'. Stem-changing regular verbs (aka "shoe verbs") can be supported by manipulating the verb stem prior to the validation of parameters and the lookup of verb endings. The regular conjugator could be incorporated into a general conjugator that handles irregular verbs.


#Credits

##Theme
-----
The main UI and templates for the site were generated from Twitter's Bootstrap 
See this page for more information on the CSS classes and components 
http://twitter.github.com/bootstrap/
