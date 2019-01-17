#coding:utf-8
import threading
#在项目外用脚本启动爬虫
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
import EventMonitor.EventMonitor.items
from EventMonitor.EventMonitor.spiders.news_spider import NewsSpider
from EventMonitor.EventMonitor.pipelines import EventmonitorPipeline
from scrapy.settings import Settings

#配置文件在这里手动实现
#下面是官方说法
#Running spiders outside projects it’s not much different.
#You have to create a generic Settings object and populate it as needed (See 内置设定参考手册 for the available settings),
#instead of using the configuration returned by get_project_settings.
#翻译
#运行蜘蛛外项目没有多少不同。
#你必须根据需要创建一个通用设置对象并填充它(见内置设定参考手册可用的设置),而不是使用配置由get_project_settings返回。
def run_newsSpider(eventKey):
	settings = Settings({
		#Spiders can still be referenced by their name if SPIDER_MODULES is set with the modules where Scrapy should look for spiders.
		#Otherwise, passing the spider class as first argument in the CrawlerRunner.
		#翻译
		#蜘蛛仍然可以引用他们的名字如果SPIDER_MODULES设置模块,Scrapy应该找蜘蛛。
		#否则,将蜘蛛CrawlerRunner类作为第一个参数。
        'BOT_NAME' : 'EventMonitor',
		'SPIDER_MODULES':['EventMonitor.EventMonitor.spiders.news_spider'],
        'NEWSPIDER_MODULE' : 'EventMonitor.EventMonitor.spiders.news_spider',

		'ROBOTSTXT_OBEY':False,
		#设置包头
        'DEFAULT_REQUEST_HEADERS' : {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en',
        },
        'SPIDER_MIDDLEWARES' : {
            'EventMonitor.EventMonitor.middlewares.EventmonitorSpiderMiddleware': 543,
        },
        'ITEM_PIPELINES': {
        'EventMonitor.EventMonitor.pipelines.EventmonitorPipeline': 300,
        }
	    })
	runner=CrawlerRunner(settings)

	d=runner.crawl("eventspider", keyword=eventKey)
	d.addBoth(lambda _: reactor.stop())
	reactor.run()
	return 0
#下面的代码仅共参考，实际上直接run_csbk() 也可以
def thread_spider(eventKey):
    print("--------------")
    run_newsSpider(eventKey)
    # threading.Thread(target=run_newsSpider(eventKey))
# if __name__ == '__main__':
#     thread_spider()