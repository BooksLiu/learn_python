# coding:utf-8

'''
题目：
判断101-200之间有多少个素数，并输出所有素数。
'''

import math

count = 0

for elem in range(101, 200):
    k = int(math.sqrt(elem))
    for divisor in range(2, k + 1):
        if elem % divisor == 0:
            break
        elif divisor == k:
            print elem
            count += 1

print "共%s" % count + "个素数"
