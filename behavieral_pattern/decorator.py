"""
decorator pattern

装饰器模式定义如下：动态地给一个对象添加一些额外的职责。

AOP(Aspect Oriented Programming)：面向切面编程
    如果几个或更多个逻辑过程中（这类逻辑过程可能位于不同的对象，不同的接口当中），有重复的操作行为，就可以将这些行为提取出来（即形成切面），进行统一管理和维护。
    举例子说，系统中需要在各个地方打印日志，就可以将打印日志这一操作提取出来，作为切面进行统一维护。
"""

# AOP log接口就是装饰器的定义，而Python的@语法部分则直接支持装饰器的使用。
def log(func):
    def warpper(*args, **kwargs):
        print("call func: {}".format(func.__name__))
        return func(*args, **kwargs)
    return warpper()

@log
def now():
    print("2019-09-09")


class House:
    door = ""
    wall = ""

    def getDoor(self):
        return self.door

    def setDoor(self, door):
        self.door = door

    def getWall(self):
        return self.wall

    def setWall(self, wall):
        self.wall = wall


class whiteHouse(House):
    def __init__(self):
        self.door = "fang dan men!"
        self.wall = "white wall"


class guGong(House):
    def __init__(self):
        self.door = "liu li men"
        self.wall = "red wall"

class houseDecorator:
    def getDoor(self):
        pass

    def getWall(self):
        pass


class picDecorator(houseDecorator):
    def __init__(self, house):
        self.house = house

    def getDoor(self):
        return self.house.getDoor() + " - fu zi -."

    def getWall(self):
        return self.house.getWall() + " -- bi zhi --"


class miroDecorator(houseDecorator):
    def __init__(self, house):
        self.house = house

    def getDoor(self):
        return self.beverage.getDoor() + " -- xiao jing zi --"

    def getWall(self):
        return self.beverage.getWall() + " -- da jing zi --"

if __name__ == '__main__':
    white_houser = whiteHouse()
    print("door: {}".format(white_houser.getDoor()))
    print("wall: {}".format(white_houser.getWall()))

    pic_houser = picDecorator(white_houser)
    print("door: {}".format(pic_houser.getDoor()))
    print("wall: {}".format(pic_houser.getWall()))

    now()