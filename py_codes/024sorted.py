# -*- coding: utf-8 -*-
# 排序算法
# 排序的核心是s比较两个元素的大小
# 如果是数字，我们可以直接比较，但如果是字符串或者两个dict，直接比较数学上的大小没有意义，因此比较过程必须通过函数抽象出来。
# Python内置的sorted()函数就可以对list进行排序(升序)

sortedList = sorted([28, 1, 39, -9, 0])
print(sortedList)

# sorted()函数是一个高阶函数，它还可以接收一个key函数来自定义排序，例如按绝对值大小排序：
absSorted = sorted([39, 9, -12, 23, 29, -76, 0, 12], key=abs)
print(absSorted)

# 对字符串排序
strSorted = sorted(['beijing', 'shanghai', 'guangzhou', 'shenzhen', 'wuhan'])
print(strSorted)

# 对tuple按名字排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0].lower()

sortedL = sorted(L, key=by_name)
print(sortedL)
