#!/usr/bin/python
#coding:utf-8
#局部变量

def func(x):

    print 'x is', x
    x = 2
    print 'Changed local x to', x

x = 50
func(x)
print 'x is still', x #使用func(x)函数后，x的值依然没有变
