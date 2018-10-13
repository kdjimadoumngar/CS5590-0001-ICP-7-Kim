
from bs4 import BeautifulSoup
import urllib.request
import os
import io

import numpy as np

#created by saria goudarzvand

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
source_code = urllib.request.urlopen(url)
plain_text = source_code
soup = BeautifulSoup(plain_text, "html.parser")
[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
all_text = soup.getText()

with io.open("input.txt", "w", encoding="utf-8") as file:
    file.write(all_text)
    # result_list = soup.findAll('div', {'class': "mw-search-result-heading"})
    # print(result_list)
    # for div in result_list:
    #     link = div.find('a')
    #     href = "https://en.wikipedia.org/wiki/Python_"+link.get('href')
    #     if (link.get('href').startswith("http")):
    #         href=link.get('href')
    #     get_data(href)


# def get_data(url):
#     source_code = urllib.request.urlopen(url)
#     plain_text = source_code
#     soup = BeautifulSoup(plain_text, "html.parser")
#     body = soup.find('div', {'class': 'mw-parser-output'})
#     file2.write(str(body.text))
#     print(body.text)
#
#     np.savetxt("input.txt")
#
# search = input('type something to search in wiki: ')
# limit = input('how many results do you want to get?: ')
#
# if not os.path.exists(search):
#     print("Creating folder " + search)
#     file2 = open(search+'.txt','a+',encoding='utf-8')
#
# search_spider(search, limit)
#
#
# import re, collections
#
#
# def tokens(text):
#     """
#     Bring all words from the body paragraph
#     """
#     return re.findall('[a-z]+', text.lower())
#
#
# WORDS = tokens(open('input.txt').read())
# WORD_COUNTS = collections.Counter(WORDS) # Dictionary
#
# # top 10 words in corpus
# print(WORD_COUNTS.most_common(10))
#
#
# def known(words):
#     """
#     Display the subset of the words in the dictionary
#     """
#     return {w for w in words if w in WORD_COUNTS}
#
#
# def edits0(word):
#     """
#     Return all strings that are zero edits away
#     from the input word (i.e., the word itself).
#     """
#     return {word}
#
#
# def edits1(word):
#     """
#     Return all strings that are one edit away
#     from the input word.
#     """
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#
#     def splits(word):
#         """
#         Return a list of all possible (first, rest) pairs
#         that the input word is made of.
#         """
#         return [(word[:i], word[i:])
#                 for i in range(len(word) + 1)]
#
#     pairs = splits(word)
#     deletes = [a + b[1:] for (a, b) in pairs if b]
#     transposes = [a + b[1] + b[0] + b[2:] for (a, b) in pairs if len(b) > 1]
#     replaces = [a + c + b[1:] for (a, b) in pairs for c in alphabet if b]
#     inserts = [a + c + b for (a, b) in pairs for c in alphabet]
#     return set(deletes + transposes + replaces + inserts)
#
#
# def edits2(word):
#     """Return all strings that are two edits away
#     from the input word.
#     """
#     return {e2 for e1 in edits1(word) for e2 in edits1(e1)}
#
#
# def correct(word):
#     """
#     Get the best correct spelling for the input word
#     """
#     # Priority is for edit distance 0, then 1, then 2
#     # else defaults to the input word itself.
#     candidates = (known(edits0(word)) or
#                   known(edits1(word)) or
#                   known(edits2(word)) or
#                   [word])
#     return max(candidates, key=WORD_COUNTS.get)
#
#
# def correct_match(match):
#     """
#     Spell-correct word in match,
#     and preserve proper upper/lower/title case.
#     """
#
#     word = match.group()
#
#     def case_of(text):
#         """
#         Return the case-function appropriate
#         for text: upper, lower, title, or just str.:
#             """
#         return (str.upper if text.isupper() else
#                 str.lower if text.islower() else
#                 str.title if text.istitle() else
#                 str)
#
#     return case_of(word)(correct(word.lower()))
#
#
# def correct_text_generic(text):
#     """
#     Correct all the words within a text,
#     returning the corrected text.
#     """
#     return re.sub('[a-zA-Z]+', correct_match, text)
#
#
# print(correct_text_generic('fianlly'))
# print(correct_text_generic('additioanl'))
#
