#!/usr/bin/env python3
# coding: utf-8
# File: crawl.py.py

from scrapy import cmdline

# def startSpider(eventKey):
projcet_name = 'eventspider'
event_list = ['中兴']

for event in event_list:
    cmdline.execute("scrapy crawl {0} -a keyword={1}".format(projcet_name, event).split())
