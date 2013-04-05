#!/usr/bin/env python
# -*- coding: utf-8 -*-
import feedparser
import pprint
from random import choice


def newsyc50():
    r = feedparser.parse('http://feeds.feedburner.com/newsyc50?format=xml')
    feed = choice(r.get('entries'))
    return '{0} ({1}) {2}'.format(feed.get('link'), *feed.get('title').rsplit(' ', 1))
