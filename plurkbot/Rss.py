#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import choice
import feedparser


get_rss_list = []


def rss_list(f):
    get_rss_list.append(f)
    return f

def only_year(feeds, year):
    result = []
    for i in feeds:
        result.append(i) if i['updated_parsed'].tm_year == 2013 else None

    return result


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
def blog_coscup():
    feeds = feedparser.parse('http://feeds.feedburner.com/coscup?format=xml').get('entries')
    feed = choice(only_year(feeds, 2003))
    return '{0} ({1})'.format(
            feed.get('link'), feed.get('title').encode('utf-8'))


@rss_list
def group_coscup():
    feeds = feedparser.parse('https://groups.google.com/group/coscup-general/feed/rss_v2_0_msgs.xml?num=50').get('entries')
    feed = choice(only_year(feeds, 2003))
    return '{0} ({1})'.format(
            feed.get('link'), feed.get('title').encode('utf-8'))


@rss_list
def pypi_latest():
    feed = choice_feed('https://pypi.python.org/pypi?%3Aaction=rss')
    return '{0} ({1}) {2} - PyPI Recent Updates'.format(
            feed.get('link'), feed.get('title').encode('utf-8'),
            feed.get('summary').encode('utf-8'))


@rss_list
def pypi_newest():
    feed = choice_feed('https://pypi.python.org/pypi?%3Aaction=packages_rss')
    return '{0} ({1}) {2} - PyPI Newest Packages'.format(
            feed.get('link'), feed.get('title'), feed.get('summary').encode('utf-8'))


@rss_list
def reddit_python():
    feed = choice_feed('http://www.reddit.com/r/Python/.rss')
    return '{0} ({1}) - Reddit / Python'.format(
            feed.get('link'), feed.get('title').encode('utf-8'))


@rss_list
def reddit_vim():
    feed = choice_feed('http://www.reddit.com/r/vim/.rss')
    return '{0} ({1}) - Reddit / Vim'.format(
            feed.get('link'), feed.get('title').encode('utf-8'))


@rss_list
def reddit_android():
    feed = choice_feed('http://www.reddit.com/r/Android/.rss')
    return '{0} ({1}) - Reddit / Android'.format(
            feed.get('link'), feed.get('title').encode('utf-8'))


@rss_list
def reddit_aws():
    feed = choice_feed('http://www.reddit.com/r/aws/.rss')
    return '{0} ({1}) - Reddit / AWS'.format(
            feed.get('link'), feed.get('title').encode('utf-8'))


@rss_list
def digiphoto_tech():
    feed = choice_feed('http://digiphoto.techbang.com/pages/techniques.rss')
    return '{0} ({1}) - DIGIPHOTO 拍攝技法'.format(
            feed.get('link'), feed.get('title').encode('utf-8'))
