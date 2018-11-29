# -*- coding:utf-8 -*-

# 另一种有序列表叫元祖，即tuple。tuple和list非常相似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字
classmates = ('Neymar','Murphy','Messi')

# 初始化后classmates这个元祖就不可变了，它也没有insert(),append()这样的方法。不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。因此，如果可能，能用tuple代替list就尽量用tuple。

# tuple的陷阱：当你定义一个tuple时，tuple必须被确定下来
t = (1,2,3)

# 如果要定义一个空的tuple，可以写成()
t = ()

# 当需要定义一个只有一个元素的tuple的时候，如果用t = (1)则只能1这个数，因为Python中的()既可以表示tuple又可以表示数学公式中的小括号，这就产生了歧义，因此Python规定在这种情况下按照小括号进行计算，计算结果自然为1。此处要写成t = (1,)来消除歧义。

# tuple在特定情况下也"可变"，但是其指向不可变
t = ('a','b',['C','D'])
t[2][0] = 'c'
t[2][1] = 'd'

# exercise
M = [['Apple','Google','Microsoft'],
     ['Alibaba','Baidu','Tencent'],
     ['Huawei','Xiaomi','Oppo']
    ]
print(M[0][1])
print(M[1][2])
print(M[2][0])



