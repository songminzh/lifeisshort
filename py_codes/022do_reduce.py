# -*- coding: utf-8 -*-

from functools import reduce

def add(x, y):
    return x + y

print('求序列中各项和：', reduce(add, [1, 3, 5, 7, 9]))

def fn(x, y):
    return x * 10 + y
print('把序列变换成整数：', reduce(fn, [1, 3, 5, 7, 9]))

def f(x, y):
    return x * y

def prod(L):
    return reduce(f, L)

if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 将字符串转换成浮点数
# '123.456' -> 123.456
def str2float(s):
    List = s.split('.') # ['123', '456']
    zheng = List[0]
    xiao = List[1]

