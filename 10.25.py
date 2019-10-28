# -*-encoding:utf-8-*-
# author:dlgamelb

"""
构造函数可以不显式声明
一个类可以有多个构造函数
构造函数
1、初始化属性
析构函数
执行顺序：对象实例化->构造函数->对象调用方法->代码跳转到具体的方法->析构函数
"""


class Person(object):
    def __init__(self):
        print('我是构造函数')

    def __del__(self):
        print('我是析构函数')

    def info(self):
        print('我是方法')


per = Person()
per.info()
