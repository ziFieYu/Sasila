#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class BaseSpider(object):
    def __init__(self):
        pass

    def process(self, page):
        pass
