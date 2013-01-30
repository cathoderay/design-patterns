from abc import ABCMeta, abstractmethod


class Subject:
    __metaclass__ = ABCMeta

    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class ConcreteSubject(Subject):
    def __init__(self):
        self._observers = []
        self.state = 42

    def attach(self, observer):
        if not observer in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self):
        for observer in self._observers:
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
    subject.attach(observer)

    subject.change_state(300)

    # a message, then, should be printed by observer
