
import nltk
import io

from nltk import word_tokenize

words = word_tokenize(open('input.txt').read())

text = word_tokenize("words")

nltk.pos_tag(text)

