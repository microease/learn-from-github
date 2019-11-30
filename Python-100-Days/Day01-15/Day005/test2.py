# coding:utf-8
# File Name：     test2
# Description :
# Author :       micro
# Date：          2019/11/30
# 正整数反转
num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)