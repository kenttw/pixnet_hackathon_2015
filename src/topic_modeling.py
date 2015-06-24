# coding: utf-8


import ijson
from gensim import corpora, models, similarities
import jieba
from jieba import analyse
import util


jieba.load_userdict("new.dict_all")
stop_words = util.load_stop_words('stopword.txt')


f = open("../spam-articles-half-a-0612.json")
import itertools
from bs4 import BeautifulSoup




objects = ijson.items(f, 'item')

count = 0
words = []
for obj in objects :
    if obj['is_spam'] == 0 and obj['content'] != None :
        soup = BeautifulSoup(obj['content'])
        
        l =[]
        for item in jieba.cut(soup.getText(),cut_all = False) :
            if len(item) < 2 or item in stop_words: continue
            else : l.append(item)
        words.append(l)
        count = count + 1
    if count > 1000000 : break

dic = corpora.Dictionary(words)
corpus = [dic.doc2bow(text) for text in words]
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
lda = models.LdaModel(corpus_tfidf, id2word=dic, num_topics=24)