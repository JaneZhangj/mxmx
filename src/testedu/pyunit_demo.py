import unittest
import requests

"""
unittest演示
"""


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        print('fixture setUp')

    def tearDown(self):
        print('fixture tear down')

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        """
        测试是否大小写正常
        :return:
        """
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        """
        测试hello world
        :return:
        """
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

        with self.assertRaises(TypeError):
            s.split(2)

    def test_baidu_api(self):
        url = 'http://www.baidu.com'
        res = requests.get(url)
        self.assertEqual(res.status_code, 200)


if __name__ == '__main__':
    # unittest.main()
    # 装载测试用例
    test_cases = unittest.TestLoader.loadTestsFromTestCase(TestStringMethods)
    # 使用测试套件并打包测试用例
    test_suit = unittest.TestSuite()
    test_suit.addTest(test_cases)
    # 运行测试套件，并返回测试结果
    test_result = unittest.TextTestRunner(verbosity=2).run(test_suit)
    # 生成测试报告
    print("运行用例数为:%s" % test_result.testsrun)
    print("失败数 %s" % len(test_result.failures))
    print("错误数 %s" % len(test_result.errors))
    print("skip %s" % len(test_result.skipped()))
