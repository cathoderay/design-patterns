# File: singleton.py
# Description: Singleton implementations



class Singleton:
    """Advantages: inheritable
       Drawbacks: throws exceptions"""
    ref = None

    def __init__(self):
        if Singleton.ref: raise(Exception)
        Singleton.ref = self



def singleton(cls):
    """Advantages: easy to use, no exceptions
       Drawbacks: outside references"""

    instances = {}
    def get_instance():
        if not cls in instances:
            instances[cls] = cls()
        return instances[cls]
    return get_instance

@singleton
class Class():
   pass



class Singleton:
    """Advantages: inheritable, no exceptions
       Drawbacks: have to call get_instance"""
    ref = None

    @classmethod
    def get_instance(cls):
        if not cls.ref: cls.ref = cls()
        return cls.ref

