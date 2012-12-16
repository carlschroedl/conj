from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

from flask import Flask
from flask import render_template
from flask import Markup

import random

Base = declarative_base()

# sentence data model, stores space separated lists of words, tags and lemmas
class Sentence(Base):
     __tablename__ = 'sentence'

     id = Column(Integer, primary_key=True)
     words = Column(String)
     lemmas = Column(String)
     tags = Column(String)

     def __init__(self, words, lemmas, tags):
         self.words = words
         self.lemmas = lemmas
         self.tags = tags

     def __repr__(self):
        return "<Sentence('%s','%s','&s')>" % (self.words, self.lemmas, self.tags)

# create a new database in memory
engine = create_engine('sqlite:///:memory:', echo=True)

metadata = Base.metadata
metadata.create_all(engine) 

Session = sessionmaker(bind=engine)
    
# create a new session and add two sentences with words, lemmas, and tags
session = Session()
session.add_all([
     Sentence('Esta situado a 8_km a el noroeste de Finsterwalde .', 'estar situar a LN_km a el noroeste de finsterwalde .', 'VAIP3S0 VMP00SM SPS00 Zu SPS00 DA0MS0 NCMS000 SPS00 NP00000 Fp'),
     Sentence('Este condado fue fundado el 25_de_agosto_de_1855 .', 'este condado ser fundar el [??:25/8/1855:??.??:??] .', 'DD0MS0 NCMS000 VSIS3S0 VMP00SM DA0MS0 W Fp')])

# flush into permanent objects
session.commit()
#----------END OF DATABASE PORTION----------

#-----------START OF HTML PORTION-----------

# creates an HTML input field with the lemma as the label to the field
def createInput(lemma):
	return Markup('<span class="sentence verb"><input type="text" id="verb" /><label for="verb">%s</label></span>') % lemma

app = Flask(__name__)

@app.route('/')
def generateOutput():
	# get a random number to filter a random sentence from database
	r = random.randint(1,2)
	# return a database object based on random number query
	test_sentence = session.query(Sentence).filter_by(id=r).first()
	# get properties from query
	words = test_sentence.words.split()
	lemmas = test_sentence.lemmas.split()
	tags = test_sentence.tags.split()
	
	# begin building output string
	output = ''
	# iterate over the three lists
	for w, l, t in zip(words, lemmas, tags):
		# if the tag at the current word starts with V create an input field
		if t[0] == 'V':
			output += createInput(str(l)) + ' '
		# otherwise add the word
		else:
			output += str(w) + ' '
	# pass the output to the html template to be rendered
	return render_template('sentence.html', sentence=output)

if __name__ == '__main__':
    app.run()