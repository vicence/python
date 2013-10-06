#!/usr/bin/python
#coding:utf-8

for i in range(100,20,-38):
    print i
else:
    print "The for loop is over"
    
while True:
    s = raw_input("Enter a something: ")
    if s == 'quit':
        break
    if len(s) < 3:
        print '不够长，再来'
        continue
print "bye bye"    