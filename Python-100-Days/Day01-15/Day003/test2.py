# coding:utf-8
# File Name：     test2
# Description :
# Author :       micro
# Date：          2019/11/30
# 练习2：百分制成绩转换为等级制成绩。
score = float(input('请输入成绩: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('对应的等级是:', grade)