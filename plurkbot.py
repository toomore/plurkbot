#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import re
import sys
import setting
from random import shuffle
from random import sample

def murmur():
    i = ['我','妳','她']
    vi = ['剛剛', '昨天', '今天', '早上', '中午', '晚上', '深夜']
    v = ['吃了', '買了', '吃完', '買完', '沒有買', '沒有吃' , '忘記買', '忘記吃']
    n = ['早餐', '午餐', '晚餐', '宵夜', '點心', '雞排', '甜不辣']

    return join_word([i, vi, v, n])

def murmur_2():
    i = ['輕輕的摸了妳的']
    n = ['臉頰', '額頭', '小酒窩', '眉毛', '耳朵']

    return join_word([i, n])

def join_word(argv):
    map(shuffle, argv)
    result = [i[0] for i in argv]

    return ''.join(result)

def post_to_plurk(content):
    s = requests.Session()
    r = s.post(
        'https://www.plurk.com/Users/login',
        verify=True,
        data={
                'nick_name': setting.NICK_NAME,
                'password': setting.PASSWORD,
                'logintoken': 1}
        )

    uid = re.search('\"user_id\": ([0-9]+),', r.content).group(1)

    s.post(
        'http://www.plurk.com/TimeLine/addPlurk',
        cookies=r.cookies,
        data={
            'uid': uid,
            'content': content,
            'qualifier': ':'
            },
        )

if __name__ == '__main__':
    #post_to_plurk(murmur())
    print sample([murmur, murmur_2], 1)[0]()
