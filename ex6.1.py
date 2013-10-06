#coding= utf-8
x = r"There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print "There are %d types of people." % 10
print y
print "Those who know %s and those who %s." % (binary, do_not)

print "I said: %r." % "There are %d types of people." % 10
print "I also said: '%s'." % "Those who know %s and those who %s." % (binary, do_not)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious ,
print "Isn't that joke so funny?! False"

w = "This is the left side of..."
e = "a string with a right side."

print w + e


print "Newlines are indicated by \n"

u"如果你想要指示某些不需要如转义符那样的特别处理的字符串，\
那么你需要指定一个自然字符串。自然字符串通过给字符串\
加上前缀r或R来指定"
print r"Newlines are indicated by \n"

#转义字符
print 'what\'s'  ' your name?'


#转义符 字符串在下一行继续
print 'what\'s'\
' your name?'
