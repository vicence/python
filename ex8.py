#coding:utf-8
#字符串都要使用双引号
formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True) #为什么True, False不需要家
                                             #双引号
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
        "I had this thing.",
        "That you could type up right.",
        "But it didn't sing.",
        "So I said goodnight."
)        
#为防止有单引号的出现，这就是为什么字符串都使用双引号的原因了
