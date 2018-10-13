import nltk

from nltk import word_tokenize

from nltk.util import ngrams

word = word_tokenize(open('input.txt').read(), encoding="utf-8")

c = 2

while c < length(token) - 2:
    word.append((token[c], token[c+1], token[c+2]))

    c+= 2

    print(word)

##################################

def word_to_ngrams(word, n, sep =''):

    return [sep.join(word[i:i+n]) for i in range(len(word)-n+1)]