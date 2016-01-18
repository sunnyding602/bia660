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
stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now'] 

#read the input
f=open('in.txt')
text=f.read().strip().lower()
f.close()


#split sentences
sentences=re.split('\.',text)
print 'NUMBER OF SENTENCES: '+ str(len(sentences))

# for each sentence
for sentence in sentences:
    
    nouns=set()

    sentence=re.sub('[^a-z\d]',' ',sentence)#replace chars that are not letters or numbers with a space
    sentence=re.sub(' +',' ',sentence).strip()#remove duplicate spaces

    #tokenize the sentence
    terms = sentence.split()

    tagged_terms=nltk.pos_tag(terms)#do POS tagging on the tokenized sentence
    print tagged_terms
    break

    for pair in tagged_terms: 
        #NN for noun
        if pair[1].startswith('NN'): nouns.add(pair[0]) 


    threegrams = ngrams(terms,3) #compute 2-grams
    
    #for each 3gram
    for tg in threegrams:  
        noun_freq = 0
        if tg[0] in nouns:
            noun_freq =  noun_freq + 1
        if tg[1] in nouns:
            noun_freq =  noun_freq + 1
        if tg[2] in nouns:
            noun_freq =  noun_freq + 1
        if tg[0] in stopwords or  tg[1] in stopwords or tg[2] in stopwords:
            continue
        if noun_freq >=2:
            print tg
    
