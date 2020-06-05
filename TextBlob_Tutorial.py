# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 13:24:39 2020

@author: pattn
"""



# from textblob lib import TextBlob method 
from textblob import TextBlob 
import nltk

string1 = TextBlob("Hello World")

string1.lower()

string1[0:5]

string2 = TextBlob("Something")

string1 + "asdasdas" + string2

#Tokenization
blob = TextBlob("Welcome to the future")
print(blob.sentences)
for words in blob.sentences[0].words:
    print(words)
    
    
blob = TextBlob("Ram is a boy")
for np in blob.noun_phrases:
    print(np)
    
    
for words, tag in blob.tags:
    print (words, tag)

#Lemmatization

blob = TextBlob("Online platforms are best")

print(blob.sentences[0].words[1])

print(blob.sentences[0].words[1].singularize())

print(blob.sentences[0].words[1].lemmatize())


from textblob import Word
w = Word("Provisions")

s = w.lemmatize()
print(s)


blob = TextBlob("Platform")

print(blob.sentences[0].words[0])

print(blob.sentences[0].words[0].pluralize())





#NGrams in TextBlob

blob = TextBlob("Snake is a poisonous creature")

for ngram in blob.ngrams(3):
    print(ngram)


#Sentiment Analysis

#Two properties: POLARITY, SUBJECTIVITY
#POLARITY --> [-1,1]
#SUBJECTIVITY --> [0,1]
    
    
blob =   TextBlob("Online portals are the best")
blob.sentiment











