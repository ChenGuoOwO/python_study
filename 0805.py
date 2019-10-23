# encoding: utf-8
# author:cg


def hi(name='yasoob'):
    def greet():
        return 'now you are in the greet() function'

    def welcome():
        return 'now you are in the welcome() function'

    if name == 'yasoob':
        return greet
    else:
        return welcome


a = hi()
print(a)

print(a())
print(hi)
print(hi())
print(hi()())

'''
开放封闭原则
封闭：已实现的功能尽量不做修改
开放：对现有的功能代码可扩展
'''


def getInfo(fuc):
    print('《Pythom自动化实战》')
    return fuc()


'''
Python中装饰器的定义：在程序运行时，增加动态功能的方式。
为已经存在的对象添加额外的功能。
'''


@getInfo
def f1():
    print('网易云课堂')


'''
步骤：
1.执行getInfo函数的时候，把被装饰的函数f1当做参数传递
2.getInfo函数的返回值会重新赋值
3.一旦结合了装饰器后，调用f1的函数其实执行的是getInfo函数的内部，原来的函数f1被覆盖
4.被装饰的函数f1重新赋值给装饰器的内部函数
'''


def outer(func):
    def inner(*args, **kwargs):
        print(args, kwargs)
        func()
    return inner
