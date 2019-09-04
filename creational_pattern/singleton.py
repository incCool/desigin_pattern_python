"""
singleton pattern
定义：保证一个类只有一个实例，并提供一个访问它的全局访问点
     Ensure a class has only one instance, and provide a global point of access to it.

@for example:
总线是计算机各种功能部件或者设备之间传送数据、控制信号等信息的公共通信解决方案之一。现假设有如下场景：
某中央处理器（CPU）通过某种协议总线与一个信号灯相连，信号灯有64种颜色可以设置，中央处理器上运行着三个线程，
都可以对这个信号灯进行控制，并且可以独立设置该信号灯的颜色。抽象掉协议细节（用打印表示），如何实现线程对信号等的控制逻辑。
加线程锁进行控制，无疑是最先想到的方法，但各个线程对锁的控制，无疑加大了模块之间的耦合。
下面，我们就用设计模式中的单例模式，来解决这个问题。
"""

import threading
import time

# __new__ method singleton pattern
class Singleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)

        return cls._instance

# Bus
class Bus(Singleton):
    lock = threading.RLock()

    def sendData(self, data):
        self.lock.acquire()
        time.sleep(3)
        print("Sending Signal Data ...{}".format(data))
        self.lock.release()

class VisitEntity(threading.Thread):
    my_bus = ""
    name = ""
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

    def run(self):
        self.my_bus = Bus()
        self.my_bus.sendData(self.name)

if __name__ == '__main__':
    for i in range(3):
        print("Entity {} begin to run ...".format(i))
        my_entity = VisitEntity()
        my_entity.setName("Entity_"+str(i))
        my_entity.start()





"""
:key

class Singleton(object):
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"): #rejection
            Singleton._instance = object.__new__(cls, *args, **kwargs)

        return Singleton._instance
s1 = Singleton()
s2 = Singleton()

if id(s1) == id(s2):
    print(True)

"""

