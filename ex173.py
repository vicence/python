#!/usr/bin/python
#coding:utf-8

from sys import argv
from os.path import exists

script, from_file, to_file = argv

if exists(to_file):
    open(to_file, 'w').write(open(from_file).read())
else:
    print "文件不存在"

open(to_file).close()
open(from_file).close()