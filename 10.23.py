# -*-encoding:utf-8-*-
# author:dlgamelb

"""
类：类是由一系列属性和方法组成
Python 2.x中默认都是经典类，只有显式继承了object才是新式类

Python 3.x中默认都是新式类，不必显式的继承object

新式类是采用广度优先搜索，旧式类采用深度优先搜索
"""


class F1(object):
    pass


"""
对象的创建-->就是类实例化的过程
三个特性：
1、对象的句柄-->区分不同的对象
f2 = F1()
f1 = F1()
2、属性
    公有属性 public
        类属性：共有的属性分离出来,属于类也属于对象，建议使用类调用
        实例属性：只属于对象
        局部变量
    私有属性 private
3、方法
"""

'''类属性和实例属性的案例代码'''


class Person(object):
    # 类属性
    gongTong = 'china'

    def __init__(self, name, age):
        # 实例属性
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def info(self):
        return 'name:{0}, age:{1}, 来自:{2}'.format(self.get_name(), self.get_age(), self.gongTong)


per = Person('chenguo', 18)
print(per.get_name(), per.get_age())

per2 = Person('lili', 20)
per2.set_age('25')
per2.set_name('lina')
print(per2.get_age()+'\n'+per2.get_name())
print(per2.info())


class Person1(object):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def info(self):
        print('信息:', list(self.kwargs.values()))


per3 = Person1(name='chenguo', age=18, city='wuhan')

per3.info()


print(Person.gongTong)
