# -*-encoding:utf-8-*-
# author:dlgamelb

"""
构造函数可以不显式声明
一个类可以有多个构造函数
构造函数
1、初始化属性
"""


class Person(object):
    def __init__(self):
        print('我是构造函数')

    def __del__(self):
        print('我是析构函数')