#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import jieba.analyse
from PIL import Image,ImageSequence
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from wordcloud import WordCloud,ImageColorGenerator
import os


def getFileList(fileDir):
    for root,dirs,files in os.walk(fileDir):
        return files

#传入参数为文件名fileName，设置词数目K
#返回结果是list:[(word1,frequency1),(word2,frequency2),(word3,frequency3)]

def getWordFrequency(eventKey,K):
    # 创建停用词list
    def stopwordslist(filepath):
        stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
        return stopwords

    # 对句子去除停用词
    def movestopwords(sentence):
        stopwords = stopwordslist('news/stopwords.txt')  # 这里加载停用词的路径
        santi_words = [x for x in sentence if len(x) > 1 and x not in stopwords]
        return santi_words

    fileList = getFileList('news/' + eventKey)
    content = ''
    for item in fileList:
        fileName = 'news/' + eventKey + '/' + item

        with open(fileName, 'r', encoding='utf-8') as f:
            print(fileName)
            line = f.readline()
            line = f.readline()
            line = f.readline()  # 第一行是标题，第二行是时间
            while line:
                content += str(line)
                line = f.readline()
    words = jieba.cut(content)
    word_list = movestopwords(words)
    words_split = " ".join(word_list)
    result = jieba.analyse.textrank(words_split, topK=K, withWeight=True)
    return result


def handleFrequency(eventKey):
    frequence = getWordFrequency(eventKey, 60)
    wordName = []
    wordFreq = []
    for item in frequence:
        wordName.append(item[0])
        wordFreq.append(item[1])
    print(wordName)
    print(wordFreq)
    return [wordName, wordFreq]

# if __name__ == '__main__':
#     handleFrequency('孟晚舟')