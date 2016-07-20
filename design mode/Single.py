# -*- coding: utf-8 -*-
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"instance"):
            cls.instance = super(Singleton,cls).__new__(cls)
        return cls.instance
a = Singleton()
b = Singleton()
a.att1= "pwq"
print b.att1
print a is b
