# -*- coding: utf-8 -*-
# @Time    : 2019/11/28 16:53
# @Author  : 洋燚
# @Email   : jasonleeyag@163.com

import sys ,unittest

class A(unittest.TestCase):
    result = {'test_001':False}
    @classmethod
    def setUpClass(cls):
        super(A, cls).setUpClass()
    def test_001(self):
        self.result['test_001'] = True

        print self.result
        #@unittest.skipIf(result['a'] == 4, '跳过')


if name == 'main':
    unittest.main()