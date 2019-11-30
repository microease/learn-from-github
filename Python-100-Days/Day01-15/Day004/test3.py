# coding:utf-8
# File Name：     test3
# Description :
# Author :       micro
# Date：          2019/11/30
#### 练习1：输入一个正整数判断是不是素数。

# > **提示**：素数指的是只能被1和自身整除的大于1的整数。
user_num = int(input("请输入你要判断的数字(正整数)"))
end = user_num * user_num
is_prime = True
for i in range(2, end + 1):
    if user_num % i == 0:
        is_prime = False
        break
if is_prime and user_num != 1:
    print('%d是素数' % user_num)
else:
    print('%d不是素数' % user_num)
