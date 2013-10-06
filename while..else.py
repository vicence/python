#!/usr/bin/python
#coding:utf-8

from sys import argv
from os.path import exists

script, filename = argv

while exists(filename):
    for i in range(1,10,2):
        print i
    break
else:
    for j in range(10,1,-1):
        print j
#j为什么无法打印出来'''
#逆序需要加步长，才能打印出来