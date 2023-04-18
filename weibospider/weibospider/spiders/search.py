# -*- coding: utf-8 -*-

from scrapy import Request, Spider
import json
import re
import json
import dateutil.parser
from scrapy_redis.spiders import RedisSpider


class SearchSpider(RedisSpider):
    name = "search_spider"
    base_url = "https://s.weibo.com/"
    redis_key = "search_spider:start_urls"

    def parse(self, response, **kwargs):
        """
        网页解析
        """
        html = response.text
        tweet_ids = re.findall(r'weibo\.com/\d+/(.+?)\?refer_flag=1001030103_" ', html)
        for tweet_id in tweet_ids:
            item = {"mid": tweet_id}
            yield item
        # for tweet_id in tweet_ids:
        #     url = f"https://weibo.com/ajax/statuses/show?id={tweet_id}"
        #     yield Request(url, callback=self.parse_tweet, meta=response.meta)
        next_page = re.search('<a href="(.*?)" class="next">下一页</a>', html)
        if next_page:
            url = "https://s.weibo.com" + next_page.group(1)
            yield Request(url, callback=self.parse, meta=response.meta)


    def parse_tweet(self, response):
        pass

    #     """
    #     解析推文
    #     """
    #     data = json.loads(response.text)
    #     item = self.parse_tweet_info(data)
    #     # item['keyword'] = response.meta['keyword']
    #     if item['isLongText']:
    #         url = "https://weibo.com/ajax/statuses/longtext?id=" + item['mblogid']
    #         yield Request(url, callback=self.parse_long_tweet, meta={'item': item})
    #     else:
    #         yield item
    #
    def parse_tweet_info(self, data):
        pass
    #     """
    #     解析推文数据
    #     """
    #     tweet = {
    #         "_id": str(data['id']),
    #         "mblogid": data['mblogid'],
    #         "created_at": dateutil.parser.parse(data['created_at']).strftime('%Y-%m-%d %H:%M:%S'),
    #         "geo": data['geo'],
    #         "ip_location": data.get('region_name', None),
    #         "reposts_count": data['reposts_count'],
    #         "comments_count": data['comments_count'],
    #         "attitudes_count": data['attitudes_count'],
    #         "source": data['source'],
    #         "content": data['text_raw'].replace('\u200b', ''),
    #         'isLongText': False,
    #         "user_id": str(data['user']['id']),
    #     }
    #     if 'page_info' in data and data['page_info'].get('object_type', '') == 'video':
    #         tweet['video'] = data['page_info']['media_info']['mp4_720p_mp4']
    #     tweet['url'] = f"https://weibo.com/{tweet['user_id']}/{tweet['mblogid']}"
    #     if 'continue_tag' in data and data['isLongText']:
    #         tweet['isLongText'] = True
    #     return tweet
    #
    def parse_long_tweet(self, response):
        pass
    #     """
    #     解析长推文
    #     """
    #     data = json.loads(response.text)['data']
    #     item = response.meta['item']
    #     item['content'] = data['longTextContent']
    #     yield item
