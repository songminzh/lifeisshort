# -*- coding: utf-8 -*-

# Python内建的filter()函数用于过滤序列。
# 和map()相似，filter()也接收一个序列，和map()不同的是，filter()把传入的函数依次作用于每一个元素，然后根据返回值True和False决定保留还是丢弃该元素。

# 在一个list中，删除偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1
oddList = list(filter(is_odd, [1,2,3,4,6,7,10,12]))
print(oddList)

# 删除序列中的空字符串
def not_empty(s):
    return s and s.strip()
notEmptyList = list(filter(not_empty, ['hi', '', 'k', '89', '', 'A']))
print(notEmptyList)

# 用filter求素數
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it) #构造新序列

for n in primes():
    if n < 1000:
        print(n)
    else:
        break



