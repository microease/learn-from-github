# coding:utf-8
# File Name：     test5
# Description :
# Author :       micro
# Date：          2019/11/30
# 练习3：输入年份判断是不是闰年。
# 目前使用的格里高利历闰年规则如下：
# 公元年分除以4不可整除，为平年。
# 公元年分除以4可整除但除以100不可整除，为闰年。
# 公元年分除以100可整除但除以400不可整除，为平年。
# 公元年分除以400可整除，为闰年。

nianfen = int(input("请输入年份"))
if (nianfen % 4 == 0 and nianfen % 100 != 0) or (nianfen % 300 == 0):
    print("闰年")
else:
    print("平年")
