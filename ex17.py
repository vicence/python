#!/usr/bin/python
#coding:utf-8

from sys import argv    #仅仅是获取参数用的
from os.path import exists #暂时不知道是什么作用

script, from_file, to_file = argv  #script,是使用argv时必备的参数

print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line too, how?
input = open(from_file)
indata = input.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exists? %r" % exists(to_file)
print exists(to_file)
print "Ready , hit RETURN to continue, CTRL-C to abort."
raw_input()

output = open(to_file, 'w')
output.write(indata)

print "Alright, all none."

output.close()
input.close()