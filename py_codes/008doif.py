# -*_ coding: utf-8 -*

age = 20
if age >= 18:
    print('you age is',age)
    print('adult')
else:
    print('boy')

age = 3
if  age >= 18:
    print('your age is',age)
    print('adult')
else:
    print('your age is',age)
    print('child')

# elif 是else if的缩写，可以使用一个或者多个elif

if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('child')

# if判断的对象x须是一个BOOL值，当x为非零数值、非空字符串非空list等，就判断为True，否则为False。


# input()返回的数据类型是str，str不能直接和整数比较，必须先把str转化为整数。Python提供了int()函数来完成这项操作。
# 因此实现一个用户输入的数用于判断时，需要这样操作：

year = input('birth:')
birth = int(year)
if birth < 2000:
    print('老年人');
else:
    print('00后')

height = 1.75
weight = 80.5

bmi = weight / (height ** 2)

if bmi <= 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
elif bmi < 32:
    print('肥胖')
else:
    print('过于肥胖')




