#!usr/bin/env python3
# -*- coding: utf-8 -*-
# 继承与多态

class Animal(object):
    def run(self):
        print('Animal')

class Dog(Animal):
    def run(self):
        print('Dog')
    
class Cat(Animal):
    def run(self):
        print('Cat')

a = Animal()
d = Dog()
c = Cat()

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))
