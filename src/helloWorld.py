import  sys

def hello_world():
    """
    第一段代码
    :return:
    """
    #todo 将来要写的复杂点
    print("hello world")

def debug_demo(): #断点调试演示
    a = 1111
    b = 2
    b = 3
    c = a + b
    print(c)
    return c

def module_demo():
    print("第三个函数")


if __name__ == '__main__':
    #hello_world()
    debug_demo()
   # module_demo
