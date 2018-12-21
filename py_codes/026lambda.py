# -*- coding: utf-8 -*-

# 匿名函数有个限制，就是只能有一个表达式。
# 不用写return，返回值就是该表达式的结果。

list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

def build(x, y):    
    return lambda: x * x + y * y

f = build(1,3)
print(f())

def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
L1 = list(filter(lambda n: n % 2 == 1, range(1, 20)))

if L == L1:
    print("成功！")
