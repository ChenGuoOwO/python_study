# -*-encoding:utf-8-*-
# author:dlgamelb

import test
"""
接口测试的维度：
1.边界值的测试
2.参数为空
3.参数的类型
4.业务
安全  性能


业务：1.功能 2.接口（js代码不能出问题，前后端交互不能出问题，场景化、流程、逻辑不能出问题，高频的用户场景）
"""


"""
try--expect--else--finally:
1.先执行try，如果执行通过，就执行else代码，最后执行finally
2.如果try执行失败，就执行except，然后直接执行finally
"""


def div(a, b):
    return a/b


try:
    div(1, 1)
except Exception as e:
    print(u'输错了')
else:
    print('pass')
finally:
    print('finally')


"""
chr()整型转换为字符串
ord()字符串转化为整型
"""

