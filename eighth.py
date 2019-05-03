# coding:utf-8
'''
题目：
输出 9*9 乘法口诀表。
'''

all = []
for i in range(1, 10):
    arr = []
    for j in range(1, 10):
        if j <= i:
            arr.append(str(i) + "*" + str(j) + "=" + str(i * j))
    all.append(arr)

for arr in all:
    for string in arr:
        print string,'\t',
    print
