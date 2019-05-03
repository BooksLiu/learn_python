# coding:utf-8
'''
题目：
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
'''

str = raw_input("请随便输入一句话：")

map = {"chinese": 0, "english": 0, "space": 0, "another": 0}

for char in str.decode("utf-8"):
    if u'\u0041' <= char <= u'\u005A' or u'\u0061' <= char <= u'\u007A':
        map["english"] += 1
    elif char == u'\u0020':
        map["space"] += 1
    elif u'\u4e00' <= char <= u'\u9fff':
        map["chinese"] += 1
    else:
        map["another"] += 1

print map
