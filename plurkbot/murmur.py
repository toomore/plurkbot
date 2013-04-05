#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import shuffle
from random import choice
from utils import join_word
from dictbase import opendict


get_murmur_list = []

actor = opendict('actor.txt')
eat = opendict('eat.txt')
time = opendict('time.txt')
food = opendict('food.txt')
store = opendict('store.txt')
MRT = opendict('MRT.txt')
gift = opendict('gift.txt')
touch = opendict('touch.txt')
memory = opendict('memory.txt')


def murmur_list(f):
    get_murmur_list.append(f)
    return f


@murmur_list
def murmur():
    return join_word([actor, time, eat, food])


@murmur_list
def murmur_2():
    i = ['輕輕的摸了妳的']

    return join_word([i, touch])


@murmur_list
def murmur_3():
    ''' 她今天在誠品看到了我，也看到了妳 '''
    shuffle(actor)
    store.extend(MRT)
    return '{0}{1}在{2}看到了{3}，也看到了{4}...'.format(
            actor[0], choice(time), choice(store), actor[1], actor[2])


@murmur_list
def murmur_4():
    ''' 我收到妳寄來的照片，過了這麼多年，還記得她嗎？'''
    new_actor = actor[1:]
    shuffle(new_actor)
    return '收到{0}寄來的{1}，過了這麼多年，還記得{2}嗎？在這令人難以忘懷的{3}...'.format(
            new_actor[0], choice(gift), new_actor[1], choice(time[1:]))

@murmur_list
def murmur_5():
    ''' 我常常刻意的走到書店，在那裡找尋妳的過去回憶 '''
    new_actor = actor[1:]
    shuffle(new_actor)
    return '我常常刻意的走到{0}，在那裡找尋{1}的{2}...'.format(
            choice(store), choice(new_actor), choice(memory))


@murmur_list
def murmur_6():
    ''' 我牽著妳的手跑過了書店，因為那天下著雨... '''
    return '我牽著妳的手跑過了{0}，因為那天下著雨...'.format(choice(store))


@murmur_list
def murmur_other():
    ''' 一個句子...  '''
    return choice(opendict('other.txt'))
