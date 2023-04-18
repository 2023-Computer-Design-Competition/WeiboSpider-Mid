# -*- coding: utf-8 -*-
# @Time    : 2023/3/5 10:56
# @Author  : TimDiana
# @FileName: test.py
# @Software: PyCharm
import requests
from fake_useragent import UserAgent
# url = "http://dev.qydailiip.com/api/?apikey=c95e8a9d76eeff7d4c11b03ca47b6f9390db2402&num=1&type=text&line=win&proxy_type=putong&sort=rand&model=all&protocol=http&address=&kill_address=&port=&kill_port=&today=false&abroad=1&isp=&anonymity="
# proxy_pool = requests.get(url)
# print(proxy_pool.text)
ua=UserAgent()


print(ua.random)