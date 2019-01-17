from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from run import thread_spider
from DataAnalysis.TrendAna import TrendData
from DataAnalysis.getWordFrequency import handleFrequency
from DataAnalysis.getSentence import getAllSentences
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'EventApp/index.html')

@csrf_exempt
def search(request):
    if request.method == 'POST':
        if request.body:
            eventKey = json.loads(request.body)['eventKey']
            if eventKey == '' or eventKey == ' ':
                return HttpResponse()
            # 启动爬虫，如果测试可以注释掉，速度很慢
            thread_spider(eventKey)
            # 数据趋势分析
            trendData = TrendData(eventKey)
            # print(trendData)
            # 词频数据，用于词云图和词频表
            freqData = handleFrequency(eventKey)
            print(freqData)
            # 获取各新闻主题句
            sentencesData = getAllSentences(eventKey)
            # 返回所有的分析数据
            analysisData = [freqData, trendData, sentencesData]

            method = request.META.get('Access-Control-Allow-Method')
            origin = request.META.get('Origin')
            response = HttpResponse(json.dumps(analysisData), content_type="application/json")
            response['Access-Control-Allow-Method'] = method
            response['Access-Control-Allow-Origin'] = '*'  # origin
            response["Access-Control-Allow-Headers"] = "X-CSRFToken, Content-Type"

            return response  # HttpResponse(json.dumps(analysisData), content_type="application/json")
        return HttpResponse()
    elif request.method == 'OPTIONS':
        method = request.META.get('Access-Control-Allow-Method')
        origin = request.META.get('Origin')
        response = HttpResponse()
        response['Access-Control-Allow-Method'] = method
        response['Access-Control-Allow-Origin'] = '*' # origin
        response["Access-Control-Allow-Headers"] = "X-CSRFToken, Content-Type"
        return response


