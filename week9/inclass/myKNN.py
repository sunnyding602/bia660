"""
A simple script that demonstrates how we classify textual data with sklearn.
"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier 
from sklearn.ensemble import RandomForestClassifier 

import re

def myStrip(sentence): 
    sentence=re.sub('[^a-z\d]',' ',sentence)#replace chars that are not letters or numbers with a space
    sentence=re.sub(' +',' ',sentence).strip()#remove duplicate spaces
    yo = sentence.split(' ')
    stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']
    aha = []
    for w in yo:
        if w in stopwords:
            ''
        else:
            aha.append(w)
    return ' '.join(aha)


#read the reviews and their polarities from a given file
def loadData(fname):
    reviews=[]
    labels=[]
    f=open(fname)
    for line in f:
        review,rating=line.strip().split('\t')  
        reviews.append(myStrip(review.lower()))    
        labels.append(int(rating))
    f.close()
    return reviews,labels

rev_test = []
labels_test = []
f=open('in.txt')
for line in f:
    rev_test.append(myStrip(line.strip().lower()))
f.close()
f2=open('correct.txt')
for line in f2:
    labels_test.append(int(line.strip())); 
f2.close()

rev_train,labels_train=loadData('train.txt')
#rev_test,labels_test=loadData('reviews_test.txt')

#Build a counter based on the training dataset
counter = CountVectorizer()
counter.fit(rev_train)

#count the number of times each term appears in a document and transform each doc into a count vector
counts_train = counter.transform(rev_train)#transform the training data
counts_test = counter.transform(rev_test)#transform the testing data

#build a 3-NN classifier on the training data

KNN=RandomForestClassifier() 
KNN.fit(counts_train,labels_train)

#use the classifier to predict
predicted=KNN.predict(counts_test)

#print the accuracy
print accuracy_score(predicted,labels_test)
