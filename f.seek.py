#!/usr/bin/python
# coding:utf-8
# f.seek()探究

import sys

script, filename = sys.argv
f = open(filename)
print f.seek(0)
