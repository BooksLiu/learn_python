# coding:utf-8

'''
题目：
打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
'''


for num in range(100, 1000):
    hundred = num / 100
    decadeRemain = num % 100
    decade = decadeRemain / 10
    unit = decadeRemain % 10

    # if num == (hundred * hundred * hundred + decade * decade * decade + unit * unit * unit):
    if num == (hundred ** 3 + decade ** 3 + unit ** 3):
        print num
