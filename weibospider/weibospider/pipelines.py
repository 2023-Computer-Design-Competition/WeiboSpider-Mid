# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
import os.path
import time
import redis
from settings import REDIS_URL


class WriterPipeline(object):
    """
    写入json文件的pipline
    """

    def __init__(self):
        self.file = None
        if not os.path.exists('../output'):
            os.mkdir('../output')

    def process_item(self, item, spider):
        """
        处理item
        """
        # if not self.file:
        #     now = datetime.datetime.now()
        #     file_name = "mid_" + now.strftime("%Y%m%d%H%M%S") + '.txt'
        #     self.file = open(f'../output/{file_name}', 'wt', encoding='utf-8')
        # line = item["mid"] + "\n"
        # self.file.write(line)
        # self.file.flush()
        mid = item["mid"]
        r = redis.from_url(REDIS_URL)
        r.lpush(f'search_spider:topics_mid_url', 'https://weibo.com/ajax/statuses/show?id=' + str(mid))
        return item
