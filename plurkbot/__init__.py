#!/usr/bin/env python
# -*- coding: utf-8 -*-
from murmur import get_murmur_list
from Rss import get_rss_list
from random import choice
import requests
import re


def post_to_plurk(content, setting):
    s = requests.Session()
    r = s.post(
        'https://www.plurk.com/Users/login',
        verify=True,
        data={
            'nick_name': setting.NICK_NAME,
            'password': setting.PASSWORD,
            'logintoken': 1,})

    uid = re.search('\"user_id\": ([0-9]+),', r.content).group(1)

    s.post(
        'http://www.plurk.com/TimeLine/addPlurk',
        cookies=r.cookies,
        data={
            'uid': uid,
            'content': content,
            'qualifier': ':'},)


def run(setting):
    all_murmur = get_murmur_list + get_rss_list * 2
    murmur_word = choice(all_murmur)()
    if setting.DEBUG:
        print murmur_word
    else:
        post_to_plurk(murmur_word, setting)
