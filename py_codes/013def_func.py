#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 自定义求绝对值
def my_abs(x):
    if x > 0:
        return x
    else:
        return -x

# 空函数
def nop():
    pass #pass即什么都不做，实际上pass可以用来作为占位符，比如限制还没想好怎么写函数的代码，就可 i先放一个pass，让代码能运行起来。

# pass还可在其他语句里
age = 10
if age > 19:
    pass #却少了pass，代码运行就会有语法错误

# 参数检查，如果参数个数不对，Python解释器会自动检查出来，并抛出typeError：
# 如 my_abs(1,2) or my_abs('A') or abs('a')

# 当传入了不恰当的参数时，内置函数abs会检查出参数错误，而我们定义的my_abs没有参数检查，会导致if语句出错，出错信息和abs不一样。所以，这个函数定义不够完善。
def func_abs(x):
    if not isinstance(x,(int, float)):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x

# 返回多个值
# import math 表示倒入math包，并允许后续代码引用包里的sin,cos等函数。
import math

def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = x - step * math.sin(angle)
    return nx, ny

# 然后，就可以同时获得返回值：

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# 但其实这是假象，Python函数返回的仍然是单一值：
r = move(100, 100, 60, math.pi / 6)
print(r)

# 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple
# 位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

# 小结
# 定义函数时，需要确定函数名和参数个数；

# 如果有必要，可以先对参数的数据类型做检查；

# 函数体内部可以用return随时返回函数结果；

# 函数执行完毕也没有return语句时，自动return None。

# 函数可以同时返回多个值，但其实就是一个tuple。

# 练习：

import math

def quadratic(a, b, c):
    for i in (a, b, c):
        if not (isinstance(i, (int, float))):
            raise TypeError('bad operand type')
    if a == 0:
        return -c / b
    else:
        delta = b**2 - 4 * a * c
        if delta < 0:
            return ('方程无实数根，但有两个共轭复根')
        elif delta == 0:
            print ('方程有一个实数根')
            return -b / (2 * a)
        else:
            x_1 = (-b + math.sqrt(delta)) / (2 * a)
            x_2 = (-b - math.sqrt(delta)) / (2 * a)
            print('方程有两个实数根')
            return x_1,x_2

#x = quadratic(2, 3, 1)
#print(x)
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
