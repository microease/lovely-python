# coding:utf-8
import os

print(os.listdir())
for a, b, c in os.walk("/Users/huxiaoyi/Desktop"):
    f = open('desktop.txt', 'a')
    f.write(" % s % s % s\n" % (a, b, c))
