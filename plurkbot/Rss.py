#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import choice
import feedparser


get_rss_list = []


def rss_list(f):
    get_rss_list.append(f)
    return f


def choice_feed(url):
    return choice(feedparser.parse(url).get('entries'))


@rss_list
def newsyc50():
    ''' http://talkfast.org/2010/07/23/a-cure-for-hacker-news-overload/ '''
    feed = choice_feed('http://feeds.feedburner.com/newsyc50?format=xml')
    return '{0} ({1}) {2}'.format(
            feed.get('link'), *feed.get('title').encode('utf-8').rsplit(' ', 1))


@rss_list
def newsyc150():
    ''' http://talkfast.org/2010/07/23/a-cure-for-hacker-news-overload/ '''
    feed = choice_feed('http://feeds.feedburner.com/newsyc150?format=xml')
    return '{0} ({1}) {2}'.format(
            feed.get('link'), *feed.get('title').encode('utf-8').rsplit(' ', 1))


@rss_list
def pypi_latest():
    feed = choice_feed('https://pypi.python.org/pypi?%3Aaction=rss')
    return '{0} ({1}) {2} - PyPI Recent Updates'.format(
            feed.get('link'), feed.get('title'), feed.get('summary').encode('utf-8'))


@rss_list
def pypi_newest():
    feed = choice_feed('https://pypi.python.org/pypi?%3Aaction=packages_rss')
    return '{0} ({1}) {2} - PyPI Newest Packages'.format(
            feed.get('link'), feed.get('title'), feed.get('summary').encode('utf-8'))


@rss_list
def reddit_python():
    feed = choice_feed('http://www.reddit.com/r/Python/.rss')
    return '{0} ({1}) - Reddit / Python'.format(
            feed.get('link'), feed.get('title'))
