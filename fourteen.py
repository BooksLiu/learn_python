# coding:utf-8

'''
题目：
将一个正整数分解质因数。
'''

import math

num = int(raw_input("请输入一个整数："))

table = [2]

# 首先计算出质因数表
for x in range(2, num):
    k = int(math.sqrt(x))
    for divisor in range(2, k + 2):
        if x % divisor == 0:
            break
        elif divisor == k or k == 1:
            table.append(x)

primeArr = []
index = 0
calNum = num
while (calNum != 1):
    if calNum % table[index] == 0:
        calNum = calNum / table[index]
        primeArr.append(str(table[index]))
        index = 0
    else:
        index += 1
if len(primeArr) != 0:
    print str(num) + "的因数分解为：", '*'.join(primeArr)
else:
    print "%s无法分解质因数" % num
