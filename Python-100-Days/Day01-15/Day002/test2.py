# coding:utf-8
# File Name：     test2
# Description :
# Author :       micro
# Date：          2019/11/30
"""
赋值运算符和复合赋值运算符

Version: 0.1
Author: 骆昊
"""

a = 10
b = 3
a += b # 相当于：a = a + b
a *= a + 2 # 相当于：a = a * (a + 2)
print(a) # 想想这里会输出什么