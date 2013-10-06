print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy."\
        %(age, height, weight)

#注意我在每行print后面加了个逗号(comma)，了吧？
#这样的话print 就不会输出新行符而结束这一行跑到下一行去了

#最后一行'6\'2"'里边有一个\'序列。单引号需要被转义，
#从而防止它被识别为字符串的结尾。
