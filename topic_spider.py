# -*- coding: utf-8 -*-
# @Time    : 2023/3/2 20:27
# @Author  : TimDiana
# @FileName: topic_spider.py
# @Software: PyCharm
import time

import requests
import json
import socks
import socket

socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 10808)
socket.socket = socks.socksocket
# keywords = ["新冠", "羊了", "阳了", "发烧", "感染", "隔离", "疫情", "病毒", "病例", "核酸"]
# keywords = ["抗原", "抗疫", "疫苗",
#             "新十条", "放开", "退烧", "无症状", "轻症", "后遗症", "阳性"]
keywords = ["阴性", "酸痛", "发热", "年轻人", "儿童",
            "老人", "口罩", "酒精", "消毒", "奥密克戎"]

for keyword in keywords:
    url = "https://google-api.zhaoyizhe.com/google-api/index/mon/sec?isValid=ads&keyword=" + keyword
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Origin': 'https://weibo.zhaoyizhe.com',
        'Pragma': 'no-cache',
        'Referer': 'https://weibo.zhaoyizhe.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }
    print(requests.get('http://ifconfig.me/ip').text)
    response = requests.request("GET", url, headers=headers)
    print(keyword)
    json.dump(response.json(), open(f"topics/{keyword}.json", "w", encoding="utf-8"), ensure_ascii=False)
    # time.sleep(5)
