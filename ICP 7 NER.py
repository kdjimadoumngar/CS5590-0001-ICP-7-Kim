import nltk

from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

word = word_tokenize(open('input.txt').read())

## Tokenization

def preprocess (sent)

    sent = nltk.word_tokenize(sent)

    sent = nltk.pos_tag(sent)

    return sent

sent = preprocess(word)

sent

