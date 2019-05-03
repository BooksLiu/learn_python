# coding:utf-8

'''
题目：
求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
'''

num = int(raw_input("请输入数字:"))
times = int(raw_input("请输入个数："))
sum = 0
for index in range(1, times + 1):
    for t in range(0, index):
        sum += num * (10 ** t)

print sum
