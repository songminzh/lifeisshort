# -*- coding: utf-8 -*-

# 运用列表生成式，可以写出非常简洁的代码
L = []
for x in list(range(1, 11)):
    L.append(x * x)
print(L)

dict = {'x' : 'A', 'y' : 'B', 'z' : 'C'}
for key, value in dict.items():
    print(key, '=', value)
    
    dict.items()]
print(L)

Arr = ['IOS', 'Swift', 'Objective-C']
Arr = [s.lower() for s in Arr]
print(Arr)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
