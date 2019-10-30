# -*-encoding:utf-8-*-
# author:dlgamelb

"""公司的要求：
1、发掘业务价值
2、更短的上线时间
3、更好的软件质量
4、更少的资源投入
5、关注用户行为
6、倡导零缺陷，最有价值的事
"""


import unittest
import selenium


class F1(unittest.TestCase):
    def setUp(self):
         print('我已经做好准备工作')

    def tearDown(self):
        print('已处理')

    def test_001(self):
        print('test001')

    def test_002(self):
        print('test002')

    def test_003(self):
        self.assertEqual(1, '1')


if __name__ == '__main__':
    unittest.main(verbosity=2)


class F2(unittest.TestCase):
    @classmethod
    def setUp(self):
        print('read')
