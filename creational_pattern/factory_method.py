'''
Factory Method -- Simple Factory Method
@author : inc
1.Factory Method
Define an interface for creating objects, and let the subclass decide which class to instantiate.
Factory Method delays the instantiation of a class to its subclasses.

Applicability
When a class doesn't know which class of the object create.

When a class wants to specify the object it creates by its subclasses.

When the class delegates the responsibility of creating an object to one of several help subclasses,
and you want to localize which help subclass is the agent.
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printPerson(self):
        pass


# Simple Factory Method
class Factory:

    def FactoryMethod(F_M='F', name='heihei', age=100):
        """ return distinct string with distinct parameter """
        if F_M == 'F':
            return Boy(name, age)
        elif F_M == 'M':
            return Girl(name, age)


class Boy(Person):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.s1 = "Manhood"

    def printPerson(self):
        print(self.name + ' ' + str(self.age) + ' ' + self.s1)


class Girl(Person):
    """Girl class"""

    def __init__(self, name, age):
        super().__init__(name, age)
        self.s2 = "Half Sky"

    def printPerson(self):
        print(self.name + ' ' + str(self.age) + ' ' + self.s2)


boy = Factory.FactoryMethod('M', 'inc', 12)
girl = Factory.FactoryMethod('F', 'rose', 13)

boy.printPerson()
girl.printPerson()
