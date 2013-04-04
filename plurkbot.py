#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import re
import sys
import setting


if __name__ == '__main__':
    ''' How to use.
        python ./plurkbot.py {username} {password} {saysomething}
    '''
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
            'content': sys.argv[3],
            'qualifier': ':'
            },
        )
