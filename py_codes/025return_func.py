# -*- coding: utf-8 -*-

# 函数作为返回值
# 高阶函数除了可以接收函数作为参数以外，还可以把函数作为结果值返回。

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 2, 3)
print('sum:', f())

# 闭包
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count() # count() = [f(1), f(2), f(3)]

print(f1())
print(f2())
print(f3())

# 利用闭包返回一个计数器函数，每次调用它返回递增整数
def createCounter():
    a = []
    def counter():
        while True:
            a.append(1)
            return len(a)
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')