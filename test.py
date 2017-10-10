#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'DS'

class  ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
class MyList(list, metaclass=ListMetaclass):
    pass

l=MyList()
l.add(1)
for a in l:
    print(a)

