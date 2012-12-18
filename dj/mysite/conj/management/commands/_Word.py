class Word:
    token = None
    lemma = None
    tag = None
    sense = None

    def __init__(self, token, lemma, tag, sense):
        self.token = token
        self.lemma = lemma
        self.tag = tag
        self.sense = sense
