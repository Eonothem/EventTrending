from FastTextRank.FastTextRank4Sentence import FastTextRank4Sentence
import codecs
import re
import os
import string


def getFileList(fileDir):
    for root,dirs,files in os.walk(fileDir):
        return files

# 传入单篇文件名fileName,获得的主题句个数K
# 返回字典:{date:[sentence1,sentence2,sentence3]}

def getSentence(fileName, K, eventKey):
    try:
        # 使用正则表达式从文件名中来匹配日期
        pattern = re.compile(r"(\d{4}-\d{1,2}-\d{1,2})")  # 定义匹配模式
        mat = re.search(pattern, fileName)
        date = mat.group(0)

        mod = FastTextRank4Sentence(use_w2v=False, tol=0.0001)
        text = ''
        f = codecs.open(fileName, mode='r', encoding='utf-8')
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            text += str(line)
            line = f.readline()
        if text == '' or text == ' ':
            return None
        sentences = mod.summarize(text, K)
        # print(sentences)
        hasEventKey = []
        i = 0
        for sentence in sentences:
            hasEventKey.append(sentence.count(eventKey.replace('事件', '')))

        maxFreq = max(hasEventKey)
        # print(hasEventKey)
        if maxFreq == 0:
            return None
        maxFreqSentence = sentences[hasEventKey.index(maxFreq)]

        if 'http://' in maxFreqSentence:
            return None

        result = {date: [maxFreqSentence]}
        return result

    except Exception as e:
        print(e)
        return None


def getAllSentences(eventKey):
    fileList = getFileList('news/' + eventKey)
    allSentences = []
    dateList = []
    for item in fileList:
        fileName = 'news/' + eventKey + '/' + item
        senteResult = getSentence(fileName, 3, eventKey)
        if senteResult != None:
            print(senteResult)
            senteDate = list(senteResult.keys())[0]
            # print(senteDate)
            # print(type(senteDate))
            if senteDate in dateList:
                for sentence in allSentences:
                    if list(sentence.keys())[0] == senteDate:
                        # print(sentence[senteDate])
                        sentence[senteDate].append(senteResult[senteDate][0])
                        # print(senteResult[senteDate][0])
            else:
                dateList.append(senteDate)
                allSentences.append(senteResult)
    print(allSentences)
    return allSentences

if __name__ == '__main__':
    getAllSentences('孟晚舟')