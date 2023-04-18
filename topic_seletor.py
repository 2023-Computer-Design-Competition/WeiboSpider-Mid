# -*- coding: utf-8 -*-
# @Time    : 2023/3/2 21:41
# @Author  : TimDiana
# @FileName: topic_seletor.py
# @Software: PyCharm

from datetime import datetime
import os
import json

time_str_1 = "2022-12-7 00:00"
time_format_1 = "%Y-%m-%d %H:%M"
timestamp_1 = datetime.strptime(time_str_1, time_format_1).timestamp()

time_str_2 = "2023-1-15 00:00"
time_format_2 = "%Y-%m-%d %H:%M"
timestamp_2 = datetime.strptime(time_str_2, time_format_2).timestamp()

print(timestamp_1)  # 输出结果为：1662537600.0
print(timestamp_2)  # 输出结果为：1673827200.0

file_names = []
topic_list = []
# 遍历目录树
for root, dirs, files in os.walk('./topics'):
    # 遍历文件
    for file in files:
        # 输出文件名
        file_names.append(os.path.basename(file))
for file in file_names:
    raw = json.load(open('./topics/' + file, 'rb'))
    datas = raw['data']
    for data in datas:
        time_str = data['date']
        time_format = "%y-%m-%d %H:%M"
        timestamp = datetime.strptime(time_str, time_format).timestamp()
        if timestamp_1 <= timestamp <= timestamp_2:
            topic_list.append(data['topic'])
with open("topics_selected.txt", 'w', encoding='utf-8') as f:
    for topic in topic_list:
        f.write(topic + "\n")
