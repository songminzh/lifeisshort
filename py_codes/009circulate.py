# -*- coding: utf-8 -*-

# for循环

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# 求和 

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print('10以内整数之和为',sum)

# 求1-100之间的整数之和

sum = 0
for x in range(101):
    sum = sum + x
print('100以内整数之和为',sum)

# 求100以内奇数之和
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print('100以内奇数之和为',sum)

# break：跳出循环，continue：跳出本次循环
















