# -*- coding: utf-8 -*-

# 生成器(Generator):对于元素量巨大的list，我们可以使用生成器.
# 用某种算法一边循环一边计算的机制创建，这样就不必创建完整的list，从而节省大量的空间。

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

# 杨辉三角形
def triangles():
    N = [1]
    while True:
        yield N
        N = N + [0]
        N = [N[i-1] + N[i] for i in range(len(N))]

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break

if results == [
               [1],
               [1, 1],
               [1, 2, 1],
               [1, 3, 3, 1],
               [1, 4, 6, 4, 1],
               [1, 5, 10, 10, 5, 1],
               [1, 6, 15, 20, 15, 6, 1],
               [1, 7, 21, 35, 35, 21, 7, 1],
               [1, 8, 28, 56, 70, 56, 28, 8, 1],
               [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
               ]:
    print('测试通过!')
else:
    print('测试失败!')








