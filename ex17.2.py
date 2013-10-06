#!/usr/bin/python
#coding:utf-8

from sys import argv
from os.path import exists

script, from_file, to_file = argv

#open(to_file, 'w').write(open(from_file).read())

txt = open(from_file)
indata = txt.read()

txt1 = open(to_file, 'w')
txt1.write(indata)

txt1.close()
txt.close()
