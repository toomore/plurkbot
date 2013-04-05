#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import choice
import feedparser


get_rss_list = []


def rss_list(f):
    get_rss_list.append(f)
    return f


@rss_list
def newsyc50():
    r = feedparser.parse('http://feeds.feedburner.com/newsyc50?format=xml')
    feed = choice(r.get('entries'))
    return '{0} ({1}) {2}'.format(
            feed.get('link'), *feed.get('title').rsplit(' ', 1))
