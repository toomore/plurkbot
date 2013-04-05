#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import shuffle


def join_word(argv):
    map(shuffle, argv)
    result = [i[0] for i in argv]

    return ''.join(result)
