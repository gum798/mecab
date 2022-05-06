# coding=utf-8
import os
import json
import MeCab
dicdir = os.path.join(os.getcwd(), 'local', 'lib', 'mecab', 'dic')
rcfile = os.path.join(os.getcwd(), 'local', 'etc', 'mecabrc')
def lambda_handler(event, context):
    #sentence = event.get('sentence', '')
    sentence = "아버지가방에들어가신다"
    t = MeCab.Tagger('-d '+dicdir)
    m = t.parseToNode(sentence)
    while m:
        print(m.surface, "\t", m.feature)
        m = m.next
    print("EOS")
	