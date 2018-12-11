# -*- coding: utf-8 -*-

# 迭代器
from collections import Iterable, Iterator
print(isinstance([], Iterable))

it = iter([1, 2, 3, 4, 5, 6])
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
