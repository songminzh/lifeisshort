#!usr/bin/env python3
# -*- coding:utf-8 -*-
# 获取对象信息：类型与属性

class MyObject(object):
    def __init__(self):
        self.x = 9
    
    def power(self):
        return self.x * self.y

print('type(123) is', type(123))
print('type(\'123\') is', type('123'))
print('type(None) is', type(None))
print('type(abs) is', type(abs))

import types

print('type(\'abc\')is str?', type('abc')==str)

obj = MyObject()
print('hasattr(obj, \'x\') =', hasattr(obj, 'x'))
print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # 有属性'y'吗？
setattr(obj, 'y', 19) # 设置一个属性'y'
print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # 有属性'y'吗？
print('getattr(obj, \'y\') =', getattr(obj, 'y')) # 获取属性'y'
print('obj.y =', obj.y) # 获取属性'y'

print('getattr(obj, \'z\') =',getattr(obj, 'z', 404)) # 获取属性'z'，如果不存在，返回默认值404

f = getattr(obj, 'power') # 获取属性'power'
print(f)
print(f())
