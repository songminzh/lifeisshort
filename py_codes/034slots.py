#!usr/bin/env python3
# -*- coding: utf-8 -*-
# Python允许在定义class的时定义一个特殊的__slots__变量来限制该class实例能添加的属性
# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的

class Student(object):
    __slots__ = ('name', 'age')

class GraduateStudent(Student):
    pass

s = Student()
s.name = 'Leo'
s.age = 22

try:
    s.score = 100
except AttributeError as e:
    print('AttributeError:', e)

g = GraduateStudent()
g.score = 99
print('g.score = ', g.score)
