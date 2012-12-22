Aprender
====

Class project for CS 545 at UW-Madison. Provides an open-source Spanish 
conjugation driller. Presents user with a sentence that has an input field in 
place of a verb in the sentence. Information on the missing verb, including 
infinitive and relevant conjugation information, is shown under the input field. 
The user is asked to fill in the correct conjugation and then press *Check 
Answer*. The user will then receive feedback on their answer and if they want to 
they can choose *Get New Exercise* to get a new random sentence from the corpus.

The *Get New Exercise* function does a GET Ajax request for a random sentence 
in the database. Our view models are also capable to accept POST requests to 
be able to select more specific sentences based on a set of boolean features 
that describe each verb.

Our UI is populated via the MVVC Knockout.js. More information can be found 
here http://knockoutjs.com/

Installation and Use
----------------
Requires Django 1.4.2 https://www.djangoproject.com/download/1.4.2/tarball/
More information on installing Django https://docs.djangoproject.com/en/dev/intro/install/

Once Django is installed you can run
```
python manage.py runserver
```
From the /dj/mysite/ directory and go to http://localhost:8000 to begin the 
exercises.

Sources
-------
We used the Wikicorpus (http://www.lsi.upc.edu/~nlp/wikicorpus/) dataset

Parsing the Wikicorpus
----------------------
The Wikicorpus parser includes a two step process that preprocesses the 
Wikicorpus dump files and then parses each document into new database objects 
as defined in /dj/mysite/conj/models.py.

To use the parser you can run
```
python manage.py insertWikiCorpus <wikicorpus dump file> <frequency pickle>
```
from the /dj/mysite/ directory

Database
--------
You can set up the database indicating the name and what type by changing the 
relevant information in /dj/conj/mysite/mysite/settings.py file
More information can be found here https://docs.djangoproject.com/en/dev/ref/databases/

Frequency Analysis
------------------
We were able to do some additional preprocessing of the wikicorpus and we were 
able to define the top 1000 most common verbs in the corpus. The human readable 
output of this analysis can be found in /freq/output.txt. We then determined 
that a verb could be defined as 'frequent' if it occurred in more than 1% of 
the corpus. This amounted to 478 verbs (out of over 86,000 total) that are 
stored in a Python dictionary object in the file freq.pkl.

Regular Conjugator
------------------
We also implemented a regular conjugator that has rules defined for regular 
verb conjugations for all tenses and moods that can label the verbs either 
regular or irregular.

Theme
-----
The main UI and templates for the site were generated from Twitter's Bootstrap 
See this page for more information on the CSS classes and components 
http://twitter.github.com/bootstrap/
