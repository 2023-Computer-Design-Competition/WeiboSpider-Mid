# -*- coding: utf-8 -*-
# @Time    : 2023/2/7 14:23
# @Author  : Lemoon
# @FileName: run_spider.py
# @Software: PyCharm
import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.search import SearchSpider

if __name__ == '__main__':
    os.environ['SCRAPY_SETTINGS_MODULE'] = 'settings'
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(SearchSpider)
    # the script will block here until the crawling is finished
    process.start()
