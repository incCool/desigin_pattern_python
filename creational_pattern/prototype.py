"""
source ip: https://yq.aliyun.com/articles/70451?spm=a2c4e.11154837.922301.9.6feb20ad5Ev7DM

定义：用原型实例指定创建对象的种类，并且通过复制这些原型创建新的对象。


"""

from copy import copy,deepcopy

# 图像对象
"""
一、图层
大家如果用过类似于Photoshop的平面设计软件，一定都知道图层的概念。图层概念的提出，使得设计、图形修改等操作更加便利。
设计师既可以修改和绘制当前图像对象，又可以保留其它图像对象，逻辑清晰，且可以及时得到反馈。本节内容，将以图层为主角，介绍原型模式。
首先，设计一个图层对象。
"""
class simpleLayer:
    background = [0, 0, 0, 0]
    content = "blank"

    def getContent(self):
        return self.content

    def getBackgroud(self):
        return self.background

    def paint(self, painting):
        self.content = painting

    def setParent(self, p):
        self.background[3] = p

    def fillBackground(self, back):
        self.background = back

    def clone(self): # 浅拷贝会拷贝对象内容及其内容的引用或者子对象的引用，但不会拷贝引用的内容和子对象本省
        """ 需要注意一点的是，进行clone操作后，新对象的构造函数没有被二次执行，新对象的内容是从内存里直接拷贝的 """
        return copy(self)

    def deep_clone(self): # 不仅拷贝了对象和内容的引用，也会拷贝引用的内容
        return deepcopy(self)

if __name__ == '__main__':
    dog_layer = simpleLayer()
    dog_layer.paint("Dog")
    dog_layer.fillBackground([0,0,255,0])
    print("Background:",dog_layer.getBackgroud())
    print("Painting:",dog_layer.getContent())

    another_dog_layer = dog_layer.clone()

    print("Background:",another_dog_layer.getBackgroud())
    print("Painting:",another_dog_layer.getContent())

