# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import MySQLdb

class EventmonitorPipeline(object):
    def __init__(self):
        CUR = '/'.join(os.path.abspath(__file__).split('/')[:-2])
        self.news_path = os.path.join(CUR, 'news')
        if not os.path.exists(self.news_path):
            os.makedirs(self.news_path)

    '''处理数据流'''
    def process_item(self, item, spider):
        #print(item)
        keyword = item['keyword']
        event_path = os.path.join(self.news_path, keyword)
        if not os.path.exists(event_path):
            os.makedirs(event_path)
        filename = os.path.join(event_path, item['news_date'] + '＠' + item['news_title'])
        try:
            print(filename)
            self.save_localfile(filename, item['news_title'], item['news_time'], item['news_content'], keyword) #保存到本地TXT文件
        except:
            print('保存至本地错误')
            pass
        # try:
        #     self.save_localdb(item['news_title'], item['news_time'], item['news_content'], keyword)             #保存到本地数据库
        # except:
        #     print('保存至数据库错误')
        #     pass
        return item

    '''将内容保存至文件当中'''
    def save_localfile(self, filename, title, pubtime, content, keyword):
        with open(filename, 'w+', encoding ='utf-8') as f:
            f.write('标题:{0}\n'.format(title))
            f.write('发布时间:{0}\n'.format(pubtime))
            f.write('正文:{0}\n'.format(content))
            time_path = os.path.join(self.news_path, "recordTime-%s" % keyword)
            with open(time_path,'a+',encoding ='utf-8') as ff:
                ff.write(pubtime + '\n')
        f.close()

    # #将内容保存到本地数据库中
    # def save_localdb(self, title, pubtime, content, keyword):
    #     # 连接数据库
    #     connect = MySQLdb.Connect(
    #         host='localhost',
    #         port=3306,
    #         user='root',
    #         passwd='root',
    #         db='newsProject',
    #         charset='utf8'
    #     )
    #     # 获取游标
    #     cursor = connect.cursor()
    #     # 插入数据
    #     sql = """INSERT INTO newsRecord (title, pubtime, content, keyword) VALUES ('%s', '%s', '%s', '%s')""" % (title,pubtime, content, keyword)
    #     try:
    #         result = cursor.execute(sql)
    #         connect.commit()
    #     except:
    #         print('保存到数据库失败！')
    #         connect.rollback()
    #     connect.close()