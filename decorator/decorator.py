from abc import ABCMeta, abstractmethod


class Component(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def do(self):
        pass


class ConcreteComponent(Component):
    def do(self):
        print "default behaviour...done"


class Decorator(Component):
    __metaclass__ = ABCMeta

    def __init__(self, component):
        self.component = component

    @abstractmethod
    def do(self):
        return 1


class ConcreteDecorator(Decorator):
    def do(self):
        self.component.do()
        print "decorating...done"


class AnotherConcreteDecorator(Decorator):
    def do(self):
        self.component.do()
        print "another decorating...done"


if __name__ == '__main__':
    c = ConcreteComponent()
    c = ConcreteDecorator(c)
    c = AnotherConcreteDecorator(c)
    c.do()
