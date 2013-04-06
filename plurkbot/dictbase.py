#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def clean_words(s):
    return map(lambda x: x.replace('\n', ''), s)

def opendict(f):
    return clean_words(file(os.path.join(os.path.dirname(__file__), './dictfile/', f)).readlines())

