from abc import ABCMeta, abstractmethod


class Subject:
    __metaclass__ = ABCMeta

    @abstractmethod
    def register(self, observer):
        pass

    @abstractmethod
    def unregister(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class ConcreteSubject(Subject):
    def __init__(self):
         self.observers = []
         self.state = 42

    def register(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def unregister(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self, self.state)

    def change_state(self, value):
       self.state = value
       self.notify()


class Observer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, sender, msg):
        pass


class ConcreteObserver(Observer):
    def update(self, sender, msg):
        print "I received a message from %s: [msg: %s]" % (sender, msg)


if __name__ == '__main__':
    subject = ConcreteSubject()
    observer = ConcreteObserver()
    subject.register(observer)

    subject.change_state(300)
    # a message, then, should be printed by observer
