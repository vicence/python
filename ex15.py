#!/usr/bin/python
#coding:utf-8

#from sys import argv
#的功能仅仅是提示我可以接受参数而已
#除此之外并无其他功能


from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print ''
print txt.read()
print txt.close()

print "I'll also ask you to type it again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
print txt_again.close()
