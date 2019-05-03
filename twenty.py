# coding:utf-8
'''
题目：
    一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''

high = float(100)
sum = 0.0
for times in range(1, 11):
    sum += high
    high = high / 2

print "共经过%f米，第10次反弹%f米高" % (sum, high)
