# -*-encoding:utf-8-*-
# author:dlgamelb


"""
方法的继承

子类可以重写父类的方法，对子类进行实例化后，子类调用的方法父类子类都存在，子类执行子类的方法

单个类继承的原则：
1、从上到下：子类继承了父类，但是子类没有重写父类的方法，那么子类实例化后，调用的方法是直接调用的父类的方法
2、从下到上原则：子类继承了父类，但是子类重写父类的方法，那么子类实例化后，调用的方法是子类当中的方法（子类优先考虑自己类的方法）
"""


class Fruit(object):
    def eat(self):
        print('水果是可以吃的')


class Apple(Fruit):
    def __init__(self, color):
        self.color = color

    def eat(self):
        print('颜色是{0}的时候，可以吃'.format(self.color))


class UsaApple(Apple):
    def __init__(self, color, brand, taste):
        super(UsaApple, self).__init__(color)  # 需要调用父类的实例属性并添加实例属性时，才使用super；super可以避免构造函数被多次调用
        self.brand = brand
        self.taste = taste

    def eat(self):
        print('美国苹果{0},{1}薄汁多，白里透{2}'.format(self.taste, self.brand, self.color))


apple = Apple('红色')
apple.eat()
uapple = UsaApple('红', '皮', '很甜')
uapple.eat()


"""
多个类的继承，总是从左到右
"""


class A(object):
    def __init__(self):
        print('enter A')
        print('leave A')


class B(A):
    def __init__(self):
        print('enter B')
        super().__init__()
        print('leave B')


class C(A):
    def __init__(self):
        print('enter C')
        super().__init__()
        print('leave C')


class D(B, C):
    def __init__(self):
        print('enter D')
        super().__init__()
        print('leave D')


d = D()
print(D.mro())

"""
MRO列表真实的列出了类C的继承顺序
事实上，super 和父类没有实质性的关联。
super(cls, inst) 获得的是 cls 在 inst 的 MRO 列表中的下一个类 
"""


class Base(object):
    def __init__(self):
        print("enter Base")
        print("leave Base")


class A(Base):
    def __init__(self):
        print("enter A")
        Base.__init__(self)  # 调用父类的构造函数进行初始化
        print("leave A")


class B(Base):
    def __init__(self):
        print("enter B")
        Base.__init__(self)  # 调用父类的构造函数进行初始化
        print("leave B")


class C(A, B):
    def __init__(self):
        print("enter C")
        A.__init__(self)  # 调用父类A的构造函数进行初始化
        B.__init__(self)  # 调用父类B的构造函数进行初始化
        print("leave C")


c = C()
print(C.mro())


class A:
    def __init__(self):
        pass

    def save(self):
        print("This is from A")


class B(A):
    def __init__(self):
        pass


class C(A):
    def __init__(self):
        pass

    def save(self):
        print("This is from C")


class D(B, C):
    def __init__(self):
        pass


fun = D()
fun.save()

# 经典类的答案： This is from A
# 新式类的答案： This is from C

