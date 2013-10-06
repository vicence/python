#!/usr/bin/python
#coding:utf-8

number = int(raw_input('Enter a chengji: '))

if (number <= 100 and number >= 90):
    print 'A'
    
elif (number < 90 and number >= 80):
    print 'B'
elif (number < 80 and number >= 70):
    print 'C'
elif (number < 70 and number >= 60):
    print 'D'
else:
    print 'E'
