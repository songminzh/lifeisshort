# -*- coding: utf-8 -*-

# 迭代（Iteration）
for ch in 'ABC':
    print(ch)

for x, y in [(1, 2), (2, 3), (3, 4)]:
    print(x, y)

# 练习（使用迭代查找一个list中的最大值和最小值，并返回一个tuple）

def findMinMax(list):
    if not(list):
        return (None,None)
    min = max = list[0]
    for n in list:
        if n < min:
            min = n
        if n > max:
            max = n
    return (min, max)

# 测试
if findMinMax([]) != (None, None):
    print('测试失败!')
elif findMinMax([7]) != (7, 7):
    print('测试失败!')
elif findMinMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
