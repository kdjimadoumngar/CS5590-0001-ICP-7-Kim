#############################Stemming#############################
import nltk
import io

from nltk import word_tokenize

from nltk.util import ngrams

with io.open('input.txt', 'r', encoding="utf-8") as file:

    words = word_tokenize(file.read())
    print(words)

# from nltk.stem import PorterStemmer
#
# from nltk.tokenize import sent_tokenize, word_tokenize
#
# ps = PorterStemmer
#
# for w in words:
#
#     print(ps.stem(w))