# coding:utf-8

'''
题目：
将一个正整数分解质因数。输出1000以内的质因数分解
'''

import math

table = [2]

# 首先计算出质因数表
for num in range(2, 1000):
    k = int(math.sqrt(num))
    for divisor in range(2, k + 2):
        if num % divisor == 0:
            break
        elif divisor == k or k == 1:
            table.append(num)

primeArr = []

for num in range(2, 1000):
    calNum = num
    index = 0
    while (calNum != 1):
        if calNum % table[index] == 0:
            calNum = calNum / table[index]
            primeArr.append(str(table[index]))
            index = 0
        else:
            index += 1
    if len(primeArr) != 0:
        print str(num) + "的因数分解为：", '*'.join(primeArr)
    primeArr = []
