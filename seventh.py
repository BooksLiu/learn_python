# coding:utf-8
'''
题目：
将一个列表的数据复制到另一个列表中。
'''
arr = [1, 2, 3, 4, 5]

copyArr = arr[:]
arr.append(6)

print copyArr
print arr
