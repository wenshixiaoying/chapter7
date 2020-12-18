#!/usr/bin/python3
#-*- coding: utf-8 -*-

import os

#get remote host environment value
def run(**kwargs):
    print('This is environment module')
    return str(os.environ)
