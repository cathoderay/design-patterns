# File: singleton.py
# Description: Singleton implementations



class Singleton:
    ref = None

    def __init__(self):
        if Singleton.ref: raise(Exception)
        Singleton.ref = self

"""
    Advantages: inheritable
    Drawbacks: throws exceptions
"""


def singleton(cls):

    instances = {}
    def get_instance():
        if not cls in instances:
            instances[cls] = cls()
        return instances[cls]
    return get_instance

@singleton
class Class():
   pass

"""
    Advantages: easy to use, no exceptions
    Drawbacks: outside references
"""


class Singleton:
    ref = None

    @classmethod
    def get_instance(cls):
        if not cls.ref: cls.ref = cls()
        return cls.ref

"""
    Advantages: inheritable, no exceptions
    Drawbacks: have to call get_instance
"""
