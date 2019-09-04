"""
@author: inc

建造者模式的定义如下：将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示
作用：将”构建“和”表示“分离，以达到解耦的作用
"""

class Food():
    name = ""
    price = 0.0
    def __init__(self):
        pass


# Burger -- mainfood

class Burger(Food):

    def __init__(self):
        super().__init__(self)

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name

class chessesBurger(Burger):
    def __init__(self):
        self.name = "chesses burger"
        self.price = 10.0

class spicyChickenBurger(Burger):
    def __init__(self):
        self.name = "spicy chicken burger"
        self.price = 15.0

# snack food
class Snack():
    pass

b1 = chessesBurger()
b1.setPrice(1.0)
print(b1.name+" "+str(b1.price))

