# coding:utf-8
'''
题目：
输入某年某月某日，判断这一天是这一年的第几天？
'''
year = int(raw_input("请输入年份（纯数字）："))
month = int(raw_input("请输入月份(纯数字)："))
day = int(raw_input("请输入日期（纯数字）："))

monthDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = 0

flag = (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0)

for index in range(1, len(monthDays)):
    if month > index:
        days = days + monthDays[index]
    else:
        days = days + day
        break

if month > 2 and flag:
    print days + 1
else:
    print days
