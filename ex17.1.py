#!/usr/bin/python
#coding:utf-8
from sys import argv

script, from_file, to_file = argv


open(to_file, 'w').write(open(from_file).read())

for line in open(to_file).readline():

    print line.readline()

open(to_file).close()
open(from_file).close()
