# -*- coding: utf-8 -*-
# @Time    : 2023/3/3 10:22
# @Author  : TimDiana
# @FileName: db_topic.py
# @Software: PyCharm
import redis
from settings import REDIS_URL
from urllib.parse import quote


def redis_init(spider_name, urls):
    r = redis.from_url(REDIS_URL)
    for key in r.scan_iter(f"{spider_name}*"):
        r.delete(key)
    print(f'Add urls to {spider_name}:start_urls')
    for url in urls:
        r.lpush(f'{spider_name}:start_urls', url)
        print('Added:', url)

def init_topic_tweets_spider():
    # topics_selected.txt中存放的是选定的话题
    urls = []
    keywords = []
    with open('../../topics_selected.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()  # 读取文件中的所有行

    for line in lines:
        # 对每行数据进行处理
        keywords.append(line.strip())  # 去除行末的换行符 '\n'

    start_time = "2022-12-01-0"  # 格式为 年-月-日-小时, 2022-10-01-0 表示2022年10月1日0时
    end_time = "2023-01-30-0"  # 格式为 年-月-日-小时, 2022-10-07-23 表示2022年10月7日23时
    for keyword in keywords:
        url = f"https://s.weibo.com/weibo?q=%23{quote(keyword)}%23&timescope=custom%3A{start_time}%3A{end_time}&page=1"
        urls.append(url)
    redis_init('search_spider', urls)


def init_keyword_tweets_spider():
    # topics_keywords.txt中存放的是关键词
    urls = []
    keywords = []
    with open('../../topics_keywords.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()  # 读取文件中的所有行

    for line in lines:
        # 对每行数据进行处理
        keywords.append(line.strip())  # 去除行末的换行符 '\n'

    start_time = "2022-12-01-0"  # 格式为 年-月-日-小时, 2022-10-01-0 表示2022年10月1日0时
    end_time = "2023-01-30-0"  # 格式为 年-月-日-小时, 2022-10-07-23 表示2022年10月7日23时
    for keyword in keywords:
        url = f"https://s.weibo.com/weibo?q={quote(keyword)}&timescope=custom%3A{start_time}%3A{end_time}&page=1"
        urls.append(url)
    redis_init('search_spider', urls)


if __name__ == '__main__':
    init_topic_tweets_spider()
