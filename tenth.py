# coding:utf-8

'''
题目：
间隔1s输出时间
'''

import time

arr = [1, 2, 3, 4]
for elem in arr:
    print elem,
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    time.sleep(1)
