import unittest


class Widget(object):
    def __init__(self, name):
        self.name = name
        self.width = 50
        self.heigth = 40

    def size(self):
        """
        计算面积
        :return:
        """
        return self.heigth * self.width

    def resize(self, heigth, width):
        """
        重新调整大小
        :param heigth:
        :param width:
        :return:
        """
        self.heigth = heigth
        self.width = width

    def dispose(self):
        print('dispose the widget')


class SimpleWidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('the widget')

    def tearDown(self):
        self.widget.dispose()

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50, 50), 'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100, 150)
        self.assertEqual(self.widget.size(), (100, 150), 'wrong size after resize')

    @unittest.skip('用于skip装饰器的示例')
    def test_skip_demo(self):
        self.assertTrue(True)


def suite():
    """
    组织测试套件
    :return:
    """
    suite = unittest.TestSuite()
    suite.addTest(SimpleWidgetTestCase('test_default_widget_size'))
    suite.addTest(SimpleWidgetTestCase('test_widget_resize'))
    return suite


if __name__ == '__main__':
    test_suite = suite()
    result = unittest.TextTestRunner(verbosity=2).run(test_suite)
