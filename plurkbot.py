#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import re
import sys

if __name__ == '__main__':
    ''' How to use.
        python ./plurkbot.py {username} {password} {saysomething}
    '''
    s = requests.Session()
    r = s.post(
        'https://www.plurk.com/Users/login',
        verify = True,
        data=
            {
                'nick_name': sys.argv[1],
                'password': sys.argv[2],
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
