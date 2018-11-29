# -*- coding: utf-8 -*-

# 递归函数
def fact(n):
    if n == 1:
        return n
    return n * fact(n - 1)

print('5! = ', fact(5))

# 尾递归函数
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print('100! = ', fact_iter(100, 1))

# 总结：使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
# 如果使用循环，程序的性能可能更高；如果使用递归，程序可能更容易理解，如何选择要看什么对你来说更重要。

# 练习(汉诺塔移动)
def hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, '-->', c)
        hanoi(n - 1, b, a, c)
hanoi(3, 'A', 'B', 'C')
