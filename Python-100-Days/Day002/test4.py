# coding:utf-8
# File Name：     test4
# Description :
# Author :       micro
# Date：          2019/11/30
# 练习2：输入圆的半径计算计算周长和面积。
import math

banjing = float(input("请输入半径："))
zhouchang = 2 * math.pi * banjing
mianji = math.pi * banjing * banjing
print("根据半径，周长为%f，面积为%f" % (zhouchang, mianji))

