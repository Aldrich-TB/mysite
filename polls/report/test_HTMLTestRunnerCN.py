#!/usr/bin/env python
# -*- coding: utf-8 -*-
import HTMLTestRunnerCN
import unittest

class testadd(unittest.TestCase):
    def setUp(self):
        pass

    def test_add1(self):
        self.assertEqual(2 + 3 + 5, 10)

    def test_add2(self):
        self.assertEqual(5, 15)

    def tearDown(self):
        pass


def suite():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(testadd("test_add1"))
    suiteTest.addTest(testadd("test_add2"))
    return suiteTest


if __name__ == '__main__':
    filePath ='E:\\mysite\\polls\\report\\test1.html'
    fp = file(filePath,'wb')
    runner = HTMLTestRunnerCN.HTMLTestRunner(
        stream=fp,
        title=u'自动化测试报告',
        description='详细测试用例结果',
        tester=u"root"
        )
    runner.run(suite())
    fp.close()