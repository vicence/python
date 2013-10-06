#coding= utf-8

#x = "There are 10 types of people."
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
#y = "Those who know binary and those who don't."
y = "Those who know %s and those who %s." % (binary, do_not)

print "There are %d types of people." % 10
print x  
print "Those who know %s and those who %s." % (binary, do_not)
print y 

print ''
print "I said: %r." % "There are %d types of people." % 10
#print "I said: ""There are %d types of people." % 10""
#上一行代入出错
print "I said: %r." % x   
print "I also said: '%s'." % "Those who know %s and those who %s." % (binary, do_not)
#print "I also said: '"Those who know %s and those who %s." % (binary, do_not)'." 
#要代入就要都代入，上一行就是错误的一行
print "I also said: '%s'." % y 
print ''

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious 
print "Isn't that joke so funny?! %r" % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print "This is the left side of..." + "a string with a right side."
print w + e


#字符串包含字符串
#y
#print y
#print "I said: %r." % x
#print "I also said: '%s'." % y
#print joke_evaluation % hilarious
#只有在代入之后才会发现这也是字符串包含字符串
