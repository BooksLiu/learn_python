# coding:utf-8
'''
题目：
输入三个整数x,y,z，请把这三个数由小到大输出。
'''

arr = []

input = raw_input("请输入三个数用英文逗号,间隔:")

strArr = input.split(",")


def translate(x):
    return int(x)


numberArr = map(translate, strArr)
numberArr.sort()

print(numberArr)
