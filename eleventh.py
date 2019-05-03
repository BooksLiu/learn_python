# coding:utf-8
'''
问题：
有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

其实就是斐波拉契数列啊
'''

arr = [1, 1]

for index in range(2, 100):
    arr.append(arr[index - 1] + arr[index - 2])

for elem in arr:
    print elem,