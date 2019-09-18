"""
Responsibility Chain Pattern
假设有这么一个请假系统：
    员工若想要请3天以内（包括3天的假），只需要直属经理批准就可以了；
    如果想请3-7天，不仅需要直属经理批准，部门经理需要最终批准；
    如果请假大于7天，不光要前两个经理批准，也需要总经理最终批准。
类似的系统相信大家都遇到过，那么该如何实现呢？
    首先想到的当然是if…else…，但一旦遇到需求变动，其臃肿的代码和复杂的耦合缺点都显现出来。
    简单分析下需求，“假条”在三个经理间是单向传递关系，像一条链条一样，因而，我们可以用一条“链”把他们进行有序连接。
"""


class request():
    req_type = "Day Off"
    days = 0


# manager: abstract
class Manager():
    higher_ups = None
    name = ""
    request = ""

    def __init__(self, name):
        self.name = name

    def setHigherUp(self, higher_ups):
        self.higher_ups = higher_ups

    def setRequest(self, request):
        self.request = request


# superior Manager
class SuperiorManger(Manager):
    # higher_ups = None
    # name = "Superior Manager"
    # request = ""

    def handleRequest(self, request):
        if request.req_type == "Day Off":
            if request.days >= 0 and request.days <= 3:
                print("Days off: {} days, superior manager allow!".format(request.days))

            if request.days > 3:
                self.setHigherUp(DepartManager)
                print("Request DepartmentManager allow.")


class DepartManager(Manager):
    def handleRequest(self, request):
        if request.req_type == "Day Off":
            if request.days > 3 and request.days <= 7:
                print("Days off: {} days, DepartmentManager allow!".format(request.days))

            if request.days > 7:
                self.setHigherUp(GenManager)
                print("Request GenManager allow.")

class GenManager(Manager):
    def handleRequest(self, request):
        if request.req_type == "Day Off":
            print("Days off: {} days, GenManager allow!".format(request.days))


if __name__ == '__main__':
    request = request()

    request.days = 7
    request.req_type = "Day Off"

    sm = SuperiorManger("Superior Manager")
    dm = DepartManager("Depart Manager")
    gm = GenManager("Gen Manager")

    sm.setHigherUp(dm)
    sm.setRequest(request)
    dm.setHigherUp(gm)
    dm.setRequest(request)

    sm.handleRequest(sm.request)
    dm.handleRequest(dm.request)



