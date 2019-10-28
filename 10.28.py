# -*-encoding:utf-8-*-
# author:dlgamelb

"""普通方法"""


class Person(object):
    def conn(self, user, pwd, host, port):
        pass

    def f1(self, *args, **kwargs):
        pass

    def info(self):
        print('我是普通方法')


per = Person()
per.info()

"""
特性方法
这个方法不能有形式参数(调用的时候不需要括号)
"""


class GetPerson(object):
    @property
    def get_user_id(self):
        print('我是特性方法')


getuser = GetPerson()
getuser.get_user_id

"""
静态方法
1、直接使用类名来进行调用
2、没有self
3、对象也可以调用静态方法
"""


class ConMysql(object):
    @staticmethod
    def conn():
        print('静态方法')


ConMysql.conn()
cm = ConMysql.conn()


"""
类方法
直接使用类来进行调用，属于类
"""


class ClassFunc(object):
    @classmethod
    def conn(cls):
        pass


"""
属于类：
    类属性
    静态方法
    类方法
属于对象：
    实例属性
    普通方法
    特性方法
"""


"""
继承：重用已经存在的数据和行为，减少代码的重复编写
1、子类继承父类所有的实例变量和方法
"""

"""类属性的继承"""


class People(object):
    come_from = '地球'

    @staticmethod
    def dream():
        print('同一个地球，同一个梦')


class UsaPeople(People):
    pass


ps = UsaPeople()
print(ps.come_from)
ps.dream()


"""实例属性的继承和继承的两种写法:可以继承，也可以不继承"""
"""子类由于业务的需求，需要继承父类的实例属性"""


class Fruit(object):
    def __init__(self, name):
        self.name = name


class Apple(Fruit):
    def __init__(self, name, brand, color):
        Fruit.__init__(self, name)
        self.brand = brand
        self.color = color

    def info(self):
        print('名称：{0}，品牌：{1}，颜色：{2}'.format(self.name, self.brand, self.color))


apple = Apple('苹果', '品牌', '红色')
apple.info()


"""子类由于业务的需求，不需要继承父类的实例属性"""


class FruitO(object):
    def __init__(self, name):
        self.name = name


class AppleO(FruitO):
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def info(self):
        print('品牌：{0}，颜色：{1}'.format(self.brand, self.color))


apple1 = AppleO('品牌', '红色')
apple1.info()
