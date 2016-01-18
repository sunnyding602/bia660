"""
@author: Ted

The script includes the following pre-processing steps for text:
- Ngrams
- POS tagging
"""
import nltk
import nltk.data
from nltk.util import ngrams
import re


#line = re.sub('(not)\s+', '\g<1>' ,line)
#read the input
f=open('in.txt')
for line in f:
    words = line.split()
    notSet = set()
    for index, word in enumerate(words):
        if 'not' == word.lower():
            notSet.add(index)
    for index, word in enumerate(words):
        if index in notSet:
            print word
        else:
            print word+' '

f.close()

