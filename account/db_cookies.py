# -*- coding: utf-8 -*-
# @Time    : 2023/2/7 12:38
# @Author  : Lemoon
# @FileName: db_cookies.py
# @Software: PyCharm

import pymongo

mongo_client = pymongo.MongoClient('mongodb://mongo:454599012@10.0.0.3:27017/')
collection = mongo_client["weibo_test"]["account"]
with open('cookies.txt', 'r') as f:
    for line in f.readlines():
        collection.insert_one({"cookie": line, "status": "available"})
