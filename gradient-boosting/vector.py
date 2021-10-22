from abc import ABC, abstractmethod
from array import array


class Vector(ABC):
    @abstractmethod
    def __add__(self, other):
        ...

    @abstractmethod
    def f(self, *args, **kwargs):
        ...


class BoolVector(Vector):
    def __init__(self, lst):
        if isinstance(lst[0], bool):
            lst = [int(x) for x in lst]
            self.vec = array('b', lst)
        else:
            raise TypeError('List contains a non-Boolean value.')

    def f(self):
        pass

    def g(self):
        pass


