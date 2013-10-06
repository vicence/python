#!/usr/bin/python
#coding:utf-8
#无法做到写完再删除
from sys import argv

script, filename = argv

input = open(filename, 'w')

input.write(raw_input('> '))

input.truncate()

input.close()