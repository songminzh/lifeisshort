# -*- coding: utf-8 -*-
# author by : murphy

# 可直接作用于for循环的对象统称为可迭代对象：Iterable
# 一类是集合数据类型，如list、tuple、dict、set、str等
# 一类是generator，包括生成器和yield的generator function

# 可使用isinstance()判断一个对象是否是iterable对象
from collections import Iterable
from collections import Iterator

isIterable = isinstance([], Iterable)
print(isIterable)

# 可使用isinstance()判断一个对象是否是Iterable对象
isIterator = isinstance((x for x in range(10)), Iterator)
print(isIterator)

# 凡事可作用于for循环的对象都是Iterable类型
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列
# 集合类型如list、dict、str等是Interable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象
# Python的for循环本质上就是通过不断调用next()函数实现的。

