#!/usr/bin/python
#coding:utf-8
#全局变量

def func():  #全局变量没有参数呢
    global x

    print 'x is', x
    x = 2
    print 'Changed local x to', x

y = 50
func()
print 'x is still', x
