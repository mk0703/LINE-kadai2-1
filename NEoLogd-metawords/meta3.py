# -*- coding: utf-8 -*-

import MeCab
import sys
import csv

m = MeCab.Tagger ("-Ochasen -d /usr/lib/mecab/dic/mecab-ipadic-neologd/")
f = open('data0v2.txt','r')
text = f.read().decode('utf-8')
f1 = open('data2v2.txt','w')
f1.write(m.parse(text.encode('utf-8')))
f.close()
f1.close()


