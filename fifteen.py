# coding:utf-8

'''
题目：
利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
'''

while True:
    num = raw_input("想结束请输入stop,请输入分数:")
    if num == 'stop':
        break
    else:
        score = int(num)
        if score >= 90:
            print num + ' is A'
        elif score >= 60:
            print num + ' is B'
        else:
            print num + ' is C'
