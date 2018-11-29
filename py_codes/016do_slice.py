# -*- coding: utf-8 -*-

# 切片
Citys = ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen', 'Wuhan', 'Nanjing', 'Hangzhou']
print('前三个城市：' , Citys[0:3])
print('最后一个城市：', Citys[-1])

L = list(range(100))
print('前十个数：', L[:10])
print('后十个数：', L[-10:])
print('11-30个数：', L[11:30])
print('前十个数，每隔两个取一个：', L[0:10:2])
print('所有数，每隔5个取一个：', L[::5])

# 练习（去除字符串首尾的空格）

def trim(str):
    while str and str[0] == ' ':
        str = str[1:]
    while str and str[-1] == ' ':
        str = str[:-1]
    return str

print('去除字符串中的空格：', trim(' intersting  '))
