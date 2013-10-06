#coding:utf-8
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


print "who is this ? %s" % backslash_cat
print "what color is the cat ? %s" % persian_cat
#%r打印出来的是你写在脚本里的内容
print "what's your name ? %r" % tabby_cat
#%s打印的是你应该看到的内容
print "what's your name ? %s" % tabby_cat

print "what weight is it ? %s" % fat_cat
