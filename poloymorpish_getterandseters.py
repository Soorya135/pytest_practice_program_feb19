class SampleClass:

    def __init__(self, a):
        ## private varibale or property in Python
        self.__a = a

    ## getter method to get the properties using an object
    def geta(self):
        return self.__a

    ## setter method to change the value 'a' using an object
    def seta(self, a):
        self.__a = a


ab = SampleClass(100)
ab.seta(100)
print(ab.geta())