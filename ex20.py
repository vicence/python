#!/usr/bin/python
# coding:utf-8
# ex20.py

from sys import argv  # 导入sys

script, input_file = argv

# 三个函数中的f，可以换成其他字符代表，并不影响函数的运行
# 其作用仅仅是提示这有个参数而已
# 真正影响的的是调用时输入的参数

def print_all(a):     # 定义print_all函数, 形参f
    print a.read()
def rewind(b):        # 定义rewind函数, 形参f
    print b.seek(0)   # 决定打印顺序,seek()使用方法未知
def print_a_line(line_count, f):  # 定义print_a_line函数, 形参line_count、f
    print line_count, f.readline()

current_file = open(input_file)

print 'First let\'s print the whole file:\n'

print_all(current_file)  # current_file = open(input_file)

print 'Now let\'s rewind, kind of like a tape.'

rewind(current_file)     # current_file = open(input_file)

print 'Let\'s print three lines:'

current_line = 1
print_a_line(current_line, current_file) # 如何知道打印哪一行

current_line += 1   # 用+=改写
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
#print open(input_file).readlines()[1]
