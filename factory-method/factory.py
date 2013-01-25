import random

from abc import ABCMeta, abstractmethod


class Product:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.state = random.randint(0, 1)

    @abstractmethod
    def tell_vendor(self):
        pass

    @abstractmethod
    def toggle(self):
        self.state = (self.state + 1) % 2


class EggProduct(Product):
    __vendor = "Eggs Corporation"

    def tell_vendor(self):
        print EggProduct.__vendor 
    
    def toggle(self):
        super(EggProduct, self).toggle()


class ScrambledProduct(EggProduct):
    category = "scrambled"


class StarProduct(EggProduct):
    category = "star"

    def toggle(self):
        pass


class SpamProduct(Product):
    __vendor = "Spams Corporation"

    def tell_vendor(self):
        print SpamProduct.__vendor

    def toggle(self):
       super(SpamProduct, self).toggle()


class BigProduct(SpamProduct):
    category = "big"


class SmallProduct(SpamProduct):
    category = "small"


class ProductsStore:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_product(self, category):
        """Subclasses should implement""" 
        pass

    def test_product(self, category):
        """factory method client"""
        product = self.create_product(category)
        before = product.state
        product.toggle()
        after = product.state
        if after != before:
            print "product is ok! =)"
        else:
            print "product is not ok, =("


class EggStore(ProductsStore):
    def create_product(self, category):
        if category == "scrambled":
            return ScrambledProduct()
        elif category == "star":
            return StarProduct()


class SpamStore(ProductsStore):
    def create_product(self, category):
        if category == "big":
            return BigProduct()
        if category == "small":
            return SmallProduct()


if __name__ == '__main__':
    EggStore().test_product('scrambled')
    EggStore().test_product('star')
    SpamStore().test_product('big')
    SpamStore().test_product('small')
