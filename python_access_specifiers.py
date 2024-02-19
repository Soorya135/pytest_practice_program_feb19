"""
public,private and protected access specifiers in python
public is by default
protected is by using "_" (single underscore)
priviet is by using "__"  (double underscore)
"""


class A:
    def __init__(self):
        self.__x = 10
        self._y = 20
        self.z = 30

    def __m1(self):
        print("I am private method")

    def _m2(self):
        print("I am protected method")

    def m3(self):
        print("I am public method")

    def display(self):
        print(self.__x)
        print(self._y)
        print(self.z)
        self.__m1()
        self._m2()
        self.m3()


a1 = A()
a1.display()