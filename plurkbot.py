#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import re
import sys
import setting
from random import shuffle
from random import choice


get_murmur_list = []

actor = ['我','妳','她']
v = ['吃了', '買了', '吃完', '買完', '沒有買', '沒有吃' , '忘記買', '忘記吃']
time = ['剛剛', '昨天', '今天', '早上', '中午', '晚上', '深夜']
n = ['早餐', '午餐', '晚餐', '宵夜', '點心', '雞排', '甜不辣']
store = ['書店', '誠品', ' 7-11 ', '電影院', '火車站', '捷運上', '公車站', '公園', '轉運站', '摩斯漢堡']
MRT = ['東門站', '頂溪站', '劍潭站', '景美站', '江子翠站']


def murmur_list(f):
    get_murmur_list.append(f)
    return f

@murmur_list
def murmur():
    return join_word([actor, time, v, n])

@murmur_list
def murmur_2():
    i = ['輕輕的摸了妳的']
    n = ['臉頰', '額頭', '小酒窩', '眉毛', '耳朵']

    return join_word([i, n])

@murmur_list
def murmur_3():
    ''' 她今天在誠品看到了我，也看到了妳 '''
    shuffle(actor)
    store.extend(MRT)
    return '{0}{1}在{2}看到了{3}，也看到了{4}'.format(actor[0], choice(time), choice(store), actor[1], actor[2])

@murmur_list
def murmur_4():
    ''' 我收到妳寄來的照片，過了這麼多年，還記得她嗎？'''
    gift = ['照片', '禮物', '信', '手札']
    new_actor = actor[1:]
    shuffle(new_actor)
    return '收到{0}寄來的{1}，過了這麼多年，還記得{2}嗎？在這令人難以忘懷的{3} ...'.format(
            new_actor[0], choice(gift), new_actor[1], choice(time[1:]))

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
    murmur_word = choice(get_murmur_list)()
    post_to_plurk(murmur_word)
