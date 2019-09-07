"""
适配器模式定义如下：将一个类的接口变换成客户端期待的另一种接口，从而使原本因接口不匹配而无法在一起工作的两个类能够在一起工作。
适配器模式和装饰模式有一定的相似性，都起包装的作用，但二者本质上又是不同的，装饰模式的结果，是给一个对象增加了一些额外的职责，而适配器模式，则是将另一个对象进行了“伪装”。


适配器模式的优点和使用场景

优点：
1、适配器模式可以让两个接口不同，甚至关系不大的两个类一起运行；
2、提高了类的复用度，经过“伪装”的类，可以充当新的角色；
3、适配器可以灵活“拆卸”。
应用场景：
1、不修改现有接口，同时也要使该接口适用或兼容新场景业务中，适合使用适配器模式。
例如，在一个嵌入式系统中，原本要将数据从Flash读入，现在需要将数据从磁盘读入，这种情况可以使用适配器模式，将从磁盘读入数据的接口进行“伪装”，以从Flash中读数据的接口形式，从磁盘读入数据。

适配器模式的缺点

1、适配器模式与原配接口相比，毕竟增加了一层调用关系，所以，在设计系统时，不要使用适配器模式。
"""


class A_Company_Staff:
    name = ""
    id = ""
    serial_number = ""

    def __init__(self, id):
        self.id = id

    def getName(self):
        print("A protocol getName method ... id: {}".format(self.id))
        return self.name

    def setName(self, name):
        print("A protocol setName method ... id: {}".format(self.id))
        self.name = name

    def getSerialNumber(self):
        print("A protocol getSerialNumber method ... id: {}".format(self.id))
        return self.serial_number

    def setSerialNumber(self, num):
        print("A protocol setSerialNumber method ... id: {}".format(self.id))
        self.serial_number = num


class B_Company_Staff:
    name = ""
    id = ""
    telephone = ""

    def __init__(self, id):
        self.id = id

    def get_name(self):
        print("B protocol get_name method ... id: {}".format(self.id))
        return self.name

    def set_name(self, name):
        print("B protocol set_name method ... id: {}".format(self.id))
        self.name = name

    def get_telephone(self):
        print("B protocol get_telephone method ... id: {}".format(self.id))
        return self.telephone

    def set_telephone(self, telephone):
        print("B protocol set_telephone method ... id: {}".format(self.id))
        self.telephone = telephone


class Company_Staff_Adapter:
    b_com = ""

    def __init__(self, id):
        self.b_com = B_Company_Staff(id)

    def getName(self):
        return self.b_com.get_name()

    def getSerialNumber(self):
        return self.b_com.get_telephone()

    def setName(self, name):
        self.b_com.set_name(name)

    def setSerialNumber(self, num):
        self.b_com.set_telephone(num)


if __name__ == "__main__":
    acpn_staff = A_Company_Staff("123")
    acpn_staff.setName("X-A")
    acpn_staff.setSerialNumber("10012345678")
    print("A Staff Name:%s" % acpn_staff.getName())
    print("A Staff Phone:%s" % acpn_staff.getSerialNumber())
    bcpn_staff = Company_Staff_Adapter("456")
    bcpn_staff.setName("Y-B")
    bcpn_staff.setSerialNumber("99987654321")
    print("B Staff Name:%s" % bcpn_staff.getName())
    print("B Staff Phone:%s" % bcpn_staff.getSerialNumber())
