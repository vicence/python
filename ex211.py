#!/usr/bin/python
#coding:utf-8
#函数可以返回东西

def add(a, b): ##帮助文件仅显示函数名，即形参
    '''return函数

    add的最后一行是return a + b, 它实现的功能是这样的：
    1. 我们调用函数时使用了两个参数： a 和 b.
    2. 我们打印出这个函数的功能，这里就是计算加法(adding)
    3. 接下来我们告诉Python让它做某个回传的动作：我们将
       a + b的值返回（return)。或者你可以这么说：“我将a和b
       加起来，再把结果返回。”
    4. Python将两个数字相加，然后当函数结束的时候，它就可以
       将a + b的结果赋予一个变量。
    '''
    print "ADDING %d + %d" % (a, b)
    return a + b
print "开始打印"
age = add(30, 5)
print "Age: %d" % age
print age
#print add.__doc__
#help(add)

