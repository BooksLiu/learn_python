# coding:utf-8
'''
题目：
企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
'''

profit = long(raw_input("请输入利润金额："))
prize = 0.0
step = [1000000L, 600000L, 400000L, 200000L, 100000L, 0L]
percentage = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]

for index in range(len(step)):
    if profit > step[index]:
        prize = prize + (profit - step[index]) * percentage[index]
        profit = step[index]

print prize
