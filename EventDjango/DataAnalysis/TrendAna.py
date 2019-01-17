import os
import jieba.analyse
from PIL import Image,ImageSequence
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from wordcloud import WordCloud,ImageColorGenerator

def getFileList(fileDir):
    for root,dirs,files in os.walk(fileDir):
        return files

def drawPlt(fileList):
    #设定字体
    font = FontProperties(fname='DataAnalysis/Songti.ttc')
    bar_width = 0.5
    dict = {}
    for item in fileList: #将传进来的列表进行统计
        date = item[0:10]
        key = str(date)
        if dict.get(key) is None:
            dict.update({key:1})
        dict[key] += 1

    X = []
    Y = []
    tmpDict = sorted(dict.keys()) #将横坐标时间排序，再将纵坐标对应横坐标
    print(tmpDict)
    for key in tmpDict:
        X.append(key)
        Y.append(dict[key])

    num = len(X)
    print(num)

    # 保留部分数据
    if(num > 50):
        X = X[-50:]
        Y = Y[-50:]
        num = len(X)
    print(num)

    fig = plt.figure(figsize=(28,10))
    plt.bar(range(num), Y, tick_label = X, width=bar_width)
    plt.xticks(rotation=50, fontproperties=font, fontsize=10)
    plt.yticks(fontsize=20)
    plt.title("事件趋势图", fontproperties=font, fontsize=30)
    plt.savefig("barChart-3.jpg", dpi=360)
    # plt.show()
    return [X, Y]

#趋势分析，传入要分析事件的文件夹位置，进行分析，得到趋势图
def TrendData(eventKey):
    fileList = getFileList('news/' + eventKey)
    print(fileList)
    dataXY = drawPlt(fileList)
    return dataXY

# if __name__ == '__main__':
#     trendData = TrendData('中兴')
#     print(trendData)