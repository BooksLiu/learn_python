# coding:utf-8
'''
题目：
一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3
编程找出1000以内的所有完数。
'''
for num in range(1, 100000):
    allX = []
    for x in range(1, num):
        if num % x == 0:
            allX.append(x)

    if sum(allX) == num:
        print(allX)
        print num