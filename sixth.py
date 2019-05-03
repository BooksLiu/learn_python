# coding:utf-8
'''
斐波拉契数列

用递归只能求第几位的具体数值

想求出一个数组用循环的方式试试
'''


def fibonacci(n, arr):
    if n == 0 or n == 1:
        arr.append(1)
        return 1
    else:
        x = fibonacci(n - 1) + fibonacci(n - 2)
        arr.append(x)
        return x


n = int(raw_input("求斐波拉契数列前n位："))

arr = [0, 1]

for i in range(0, n):
    if i > 1:
        arr.append(arr[i - 1] + arr[i - 2])

print arr
