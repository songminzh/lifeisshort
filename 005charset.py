# 在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言
print('包含中文的string')

# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
ord_m = ord('M')
ord_zheng = ord('郑')

chr_66 = chr(66)
chr_27481 = chr(27481)

print('ord_m = ',ord_m)
print('ord_zheng = ',ord_zheng)
print('chr_66 = ',chr_66)
print('chr_27481 = ',chr_27481)

print('\u4e2d\u6587')

# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。

# Python对bytes类型的数据用带b前缀的单引号或双引号表示

x = b'ABC'

# 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节

'ABC'.encode('ascii')

'中文'.encode('utf-8')

# 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法

b'ABC'.decode('ascii')

b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

# 要计算str包含多少个字符，可以用len()函数：
len('ABC')
len('中文')

len(b'ABC')
len('中文'.encode('utf-8'))

# 可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 格式化
# %d : 整数 %f:浮点数 %s:字符串 %x:十六进制数
'Hello, %s' % 'World'



