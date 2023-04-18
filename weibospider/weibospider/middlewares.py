# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
import time
import pymongo
import scrapy.log

from settings import MONGO_URL
from fake_useragent import UserAgent


class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        ua = UserAgent()
        request.headers['User-Agent'] = ua.random
        # scrapy.log.logger.DEBUG('User-Agent: ' + request.headers['User-Agent'])

class CookieMiddleware(object):
    """
    get random cookie from account pool
    """

    def __init__(self):
        client = pymongo.MongoClient(MONGO_URL)
        self.account_collection = client['weibo_test']['account']

    def process_request(self, request, spider):
        all_count = self.account_collection.count()
        if all_count == 0:
            raise Exception('Current account pool is empty!! The spider will stop!!')
        random_index = random.randint(0, all_count - 1)
        random_account = self.account_collection.find({})[random_index]
        # While the account is waiting, sleep 5 seconds
        if random_account["status"] == "waiting":
            time.sleep(60)
            self.account_collection.find_one_and_update({'cookie': random_account['cookie']},
                                                        {'$set': {'status': 'available'}}, )
        request.headers.setdefault('Cookie', random_account['cookie'])
        request.meta['account'] = random_account


class RedirectMiddleware(object):
    """
    check account status
    HTTP Code = 302/418 -> cookie is expired or banned, and account status will change to 'error'
    """

    def __init__(self):
        client = pymongo.MongoClient(MONGO_URL)
        self.account_collection = client['weibo_test']['account']

    def process_response(self, request, response, spider):
        http_code = response.status
        if http_code == 302 or http_code == 403:
            print('account error!!!!!!!!!!!!!!')
            self.account_collection.find_one_and_update({'cookie': request.meta['account']['cookie']},
                                                        {'$set': {'status': 'waiting'}}, )
            time.sleep(10)
            return request
        elif http_code == 418:
            print('IP error!!!!!!!!!!!!!!!!!!')
            spider.logger.error('IP Proxy is invalid, please change the ip proxy or stop the programme!')
            time.sleep(10)
            return request
        else:
            return response


class IPProxyMiddleware(object):

    def fetch_proxy(self):
        # You need to rewrite this function if you want to add proxy pool
        # the function should return a ip in the format of "ip:port" like "12.34.1.4:9090"
        # url = "http://dev.qydailiip.com/api/?apikey=c95e8a9d76eeff7d4c11b03ca47b6f9390db2402&num=1&type=text&line=win&proxy_type=putong&sort=1&model=all&protocol=https&address=&kill_address=&port=&kill_port=&today=false&abroad=1&isp=&anonymity=0"
        # proxy_pool = requests.get(url)
        # return proxy_pool.text
        pass

    def process_request(self, request, spider):
        proxy_data = self.fetch_proxy()
        if proxy_data:
            current_proxy = f'http://{proxy_data}'
            spider.logger.debug(f"current proxy:{current_proxy}")
            request.meta['proxy'] = current_proxy
