# coding:utf-8
'''
题目：
输出指定格式的日期。
'''
import datetime
import time

# 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
print datetime.datetime.today().strftime("%d/%m/%Y %H:%M:%S")

# 创建日期对象
spDate = datetime.date(1965, 1, 3)
print spDate

# 日期算术运算
print spDate + datetime.timedelta(weeks=1)

# 日期替换
newSpDate = spDate.replace(year=spDate.year + 1)
print(newSpDate)
