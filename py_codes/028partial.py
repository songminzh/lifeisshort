# -*- coding: utf-8 -*-

import functools

# 当函数的参数太多而需要简化时，使用可以创建一个新的函数
# 这个新函数可以固定住原函数的部分参数，从而在调用时更简单

int2 = functools.partial(int, base = 2)

print('1000000 =', int2('1000000'))
print('1010101 =', int2('1010101'))