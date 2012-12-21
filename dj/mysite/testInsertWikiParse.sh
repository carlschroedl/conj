#!/bin/bash
rm mydatabase
python manage.py syncdb --noinput;
python -m pdb manage.py insertWikiCorpus $1 freqDict.pkl
