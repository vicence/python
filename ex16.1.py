#!/usr/bin/python
#coding:utf-8

from sys import argv

script, filename = argv

txt = open(filename, 'w')
line1 = raw_input('line 1: ')


txt.truncate()
txt.write(line1)
txt.write('\n')
txt.close()
