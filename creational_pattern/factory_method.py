'''
Factory Method
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

class Boy:

    def __init__(self):
        self.trans = dict(boy=u"男生",girl=u"女孩")

    def get(self, F_OR_M):
        '''logic process'''
        return self.trans[F_OR_M]


class Girl:
    """Simply echoes the msg ids"""
    def __init__(self):
        self.trans = dict(boy=u"男生",girl=u"女孩")
    def get(self, F_OR_M):
        return self.trans[F_OR_M]


def FactoryMethod(F_M="Boy"):
    """ return distinct string with distinct parameter """
    f_m = dict(Boy=Boy, Girl=Girl)
    return f_m[F_M]()


# Create our localizers
e, g = FactoryMethod("Boy"), FactoryMethod("Girl")

print(g.get('girl'))
