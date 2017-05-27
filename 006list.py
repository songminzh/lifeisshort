# list:有序集合，可以随时添加喝删除其中的元素。
classmates = ['Neymar','Murphy','Messi']
len(classmates)
classmates[0]
classmates[2]

# 可以用负数作索引，下标为-1代表最后一个元素，以此类推，但不能越界
classmates[-1]

# list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('Alex')

# 也可以把插入到指定位置
classmates.insert(1,'Jack')

# 可用pop()方法删除末尾的元素
classmates.pop()

# 删除指定位置的元素，用pop(i)方法，i为索引的位置
classmates.pop(2)

# 要替换某个元素，直接根据索引赋值即可
classmates[1] = 'sara'

# list中的元素的数据类型可以不同
L = ['Apple',23,True]

# list中可以嵌套list
M = ['python','java',['OC','swift'],'php'] # 也即：
iOS = ['OC','Swift']
M = ['python','java',iOS,'php']
# 要拿到'swift'可以用iOS[1]或者M[2][1]，因此可以将M看成一个二维数组


