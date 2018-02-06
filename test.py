# Filename : test.py
# coding=utf-8
__author__ = 'wind'

print ('hello world')

#事实上Python 为了优化速度，使用了小整数对象池，避免为整数频繁申请和销毁内存空间。而Python 对小整数的定义是 [-5, 257)，
#只有数字在-5到256之间它们的id才会相等，超过了这个范围就不行了，同样的道理，字符串对象也有一个类似的缓冲池，超过区间范围内自然不会相等了
#如果你需要某个
# Python 函数或语句的快速信息帮助，
# 那么你可以使用内建的 help 功能。
# 尤其在你使用带提示符的命令行的时候，
# 它十分有用。比如，运行 help(str)——这会显示 str 类的帮助
# help(str)


#我几乎可以保证你在每个
#  Python 程序中都要用到字符串，
# 所以请特别留心下面 这部分的内容。
# 下面告诉你如何在 Python 中使用字符串。
print (r'what\'s your name')

#自然字符串 R
#Unicode 字符串v u
# 字符串是不可变的
# 按字面意义级连字符串

print (r'what\'s' 'your name?')


i=5
print i
i=i+1
print i

# 运算符与表达式
# 幂运算 **
print 3**4
# 取整
print 10//7
# 取余
print 10%7
# 左移
print 2<<3
# 右移
print 16>>3
# 按位与
print 5&3
# 按位或
print  5|3
# 按位异或
print  5^3
# 按位翻转
# not 布尔非  and 布尔与

def foo():
    print 'foo click'


#foo()

#动态语言#
a = 5

print a

def foo():
    a = 10
    if(a>10):
        print 'hellp more than 10'
    elif 5<a<10 :

        print "hello less than 10"
    else:
        print 'equal'

foo()

arr = [1,2,3,4]

#循环 迭代器
for i in range(10) :
    print  i

#def  函数 申明符
def sum (a,b):
    return a+b

print sum(10,2)


#lambda   匿名 函数
aa = lambda x,y:x+y

print  aa(3,3)

print 'abcd ' + 'efgh'

# class 类

class footall(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def say(self):
        print  self.name
        print  self.age

fo = footall('laowu',12)

fo.say()

#内建函数  不需要import 的 或者对象   如input ,,raw_input

# s = raw_input('请输入年龄')
#
# print ('输入的年龄为'+s)

#input  只能接收python 表达式即你输入字符串的时候必须使用引号将它括起来
s = input('请输入一个任意的东西')

print ('任意的东西 为 '+s)

#文件 io 操作  file  open
#file 是一个类型 类似于int ,dict 可以直接实例对象。
#open 是一个内建函数 作用是根据参数来生成一个file 类型并返回 推荐使用open。

# f = open('test.py','r')
#
# for i in f:
#     print i
#
# f.close()


#map rediucs os


#d对象属性检查
#isinstance() 检查对象的类型
#hassattr() 判断对象是否有某个属性
#type() 查看对象的类型
#id() 获取对象的内存位置


ssss = 12

if (ssss.isinstance(int)):
    print ('sss is int')
