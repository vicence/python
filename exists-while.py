#!/usr/bin/python
#coding:utf-8
#文件存在则清空
from sys import argv
from os.path import exists

script, to_file = argv
while exists(to_file):
    input = open(to_file, 'w')
    input.truncate()
    input.close()
    break
else:
    print 'Game Over'