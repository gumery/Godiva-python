#!/usr/bin/env python
# coding=utf-8

import requests
import random
import json

def randomPhone():
    # 第二位数字
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]

    # 第三位数字
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),

    }[second]
    
    # 最后八位数字
    suffix = random.randint(9999999,100000000)

    # 拼接手机号
    return "1{}{}{}".format(second, third, suffix)

#限制一下请求次数, 先来100次
count = 0
limit = 100
while True:
    phone = randomPhone()
    count += 1
    if count > limit:
        break

    #调用短信发送
    url="";

    #构造请求参数
    param = json.dumps({'mobile' : phone});

    info = {
        'param' :param
    }
    retval = requests.post(url, data=info)

    print phone + retval
