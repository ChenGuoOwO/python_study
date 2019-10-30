# -*-encoding:utf-8-*-
# author:dlgamelb

"""
__doc__:打印类的注释
"""


class Person(object):
    """对人的定义"""
    def info(self, uname, upwd):  # 获取用户的信息
     pass


"""
__call__:对象创建时直接返回__call__的内容，使用该方法可以模拟静态方法
"""


class P1(object):
    def __new__(cls, *args, **kwargs):
        print('call方法')


"""
__str__:对象代表的含义，返回一个字符串，通过它可以把对象和字符串关联起来，方便某些程序的实现，该字符串表示某个类，实现了__str__后，可以直接使用print语句输出对象，也可以通过函数str来触发__str__的执行
"""


class Son(object):
    '''我是一个类'''
    def __str__(self):
        return self.__doc__


s = Son()
print(s.__str__())
print(str(s))

"""
我们至少需要添加一个 repr 方法来保证类到字符串的自定义转化的有效性，str 是可选的。因为默认情况下，在需要却找不到 str 方法的时候，会自动调用 repr 方法
当我们想所有环境下都统一显示的话，可以重构__repr__方法；当我们想在不同环境下支持不同的显示，例如终端用户显示使用__str__，而程序员在开发期间则使用底层的__repr__来显示，实际上__str__只是覆盖了__repr__以得到更友好的用户显示
"""
