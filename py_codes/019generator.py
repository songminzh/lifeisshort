# -*- coding: utf-8 -*-

# 生成器(Generator)

L = [x * x for x in range(10)] # list

g = (x * x for x in range(10)) # generator

for n in g:
    print(n)

# 斐波拉契数列（Fibonacci）

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'Done'







