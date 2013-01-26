from abc import ABCMeta, abstractmethod


class Strategy:
    __metaclass__ = ABCMeta

    @abstractmethod
    def do(self):
        pass 


class DefaultStrategy(Strategy):
    @classmethod
    def do(cls):
        print "[%s] done" % cls


class Strategy2(Strategy):
    @classmethod
    def do(cls):
        print "[%s] done" % cls
 

class StrategiesClient:
    __strategy = DefaultStrategy

    def change_strategy(self, strategy):
        self.__strategy = strategy

    def do(self):
        self.__strategy.do()


if __name__ == '__main__':
    sc = StrategiesClient()
    sc.do()
    sc.change_strategy(Strategy2)
    sc.do()
