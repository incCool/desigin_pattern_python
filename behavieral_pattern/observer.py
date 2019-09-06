"""
observer pattern

观察者模式也叫发布-订阅模式，其定义如下：定义对象间一种一对多的依赖关系，使得当该对象状态改变时，所有依赖于它的对象都会得到通知，并被自动更新。
观察者模式的通知方式可以通过直接调用等同步方式实现（如函数调用，HTTP接口调用等），也可以通过消息队列异步调用（同步调用指被观察者发布消息后，
必须等所有观察者响应结束后才可以进行接下来的操作；异步调用指被观察者发布消息后，即可进行接下来的操作。）。
事实上，许多开源的消息队列就直接支持发布-订阅模式，如Zero MQ等。
"""


# observer

class Observer:
    def update(self):
        pass


class AlarmSensor(Observer):
    def update(self, action):
        print("Alarm Got: %s" % action)
        self.runAlarm()

    def runAlarm(self):
        print("Alarm Ring...")


class WaterSprinker(Observer):
    def update(self, action):
        print("Sprinker Got: %s" % action)
        self.runSprinker()

    def runSprinker(self):
        print("Spray Water...")


class EmergencyDialer(Observer):
    def update(self, action):
        print("Dialer Got: %s" % action)
        self.runDialer()

    def runDialer(self):
        print("Dial 119...")


# 被观察者

class Observed:
    observers = []
    action = ""

    def addObserver(self, observer):
        self.observers.append(observer)

    def notifyAll(self):
        for obs in self.observers:
            obs.update(self.action)


class smokeSensor(Observed):
    def setAction(self, action):
        self.action = action

    def isFire(self):
        return True


if __name__ == "__main__":
    alarm = AlarmSensor()
    sprinker = WaterSprinker()
    dialer = EmergencyDialer()

    smoke_sensor = smokeSensor()
    smoke_sensor.addObserver(alarm)
    smoke_sensor.addObserver(sprinker)
    smoke_sensor.addObserver(dialer)

    if smoke_sensor.isFire():
        smoke_sensor.setAction("On Fire!")
        smoke_sensor.notifyAll()
