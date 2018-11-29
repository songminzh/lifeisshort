#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 位置参数
# 计算x^2的方法
def power(x):
    return x * x

x = power(10)
print('10的平方为：', x)

# 计算x^n的方法
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

a = power(2, 10)
print('2的n次方为：', a)

# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

x1 = power(2)
x2 = power(2, 9)
print(x1, x2)

# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum

# *nums表示把nums这个list的所有元素作为可变参数传进去，可变参数允许你传入0个或任意个参数
nums = [1, 2, 3]
sumOfItems = calc(*nums)
print('sum of items:', sumOfItems)

# 关键字参数(可变参数为字典)
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'others:', kw)

extra = {'city': 'Beijing', 'job' : 'Engineer'}
person('murphy', '27', **extra)

# 命名关键字参数
# 参数中用*代表命名关键字参数，用以限制关键字参数的名字
def person(name, age, *, city, job):
    print(name, age, city, job)

person('Alisa', 24, city='Hefei', job='Engineer')

# 在Python中，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a, b, c = 0, *args, **kw):
    print('a = ', age, 'b = ', b, 'c = ', c, 'args = ',args, 'kw = ', kw)
def f2(a, b, c = 0, *, d, **kw):
    print('a = ', age, 'b = ', b, 'c = ', c, 'd = ',d, 'kw = ', kw)

# 练习
def product(a, *nums):
    result = a
    for n in nums:
        result = result * n
    return result

# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
