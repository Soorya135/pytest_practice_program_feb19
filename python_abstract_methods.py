"""
Abstract metjods are methods that are declared, but contains no implementation.
"""

#class Webdriver is an abstract class and inside that we can have method like click and mouseover which
#defintion are different based on the browsers,this is the use of abstract clas


from abc import ABC, abstractmethod


class Test(ABC):

    def __init__(self):
        print("Inside constructor Parent")

    @abstractmethod
    def method1(self):
        pass


class Abstractuage(Test):

    def method1(self):
         print("defining the abstract method definition")

    def test(self):
        print("test method")


obj1 = Abstractuage()
obj1.method1()
