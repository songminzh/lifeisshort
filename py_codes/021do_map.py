# -*- coding: utf-8 -*-

def f(x):
    return x * x

print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# 将数组中的字符串变成首字母大写
def normalize(name):
    firstLetter = name[:1]
    return firstLetter.upper() + name[1:]

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
