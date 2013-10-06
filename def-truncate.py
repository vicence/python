#!/usr/bin/python
#coding:utf-8

from sys import argv
from os.path import exists
script, filename = argv

def truncate_def(filename):

    txt = open(filename, 'w')
    txt.truncate()
    txt.close()

if exists(filename):#验证文件存在否
    truncate_def(filename)#存在就删除
else:
    print '文件不存在'#不存在就提示用
#函数参数无法做到直接使用任意一个
