class sample:

    def __init__(self, a):
        self.a = a

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        if a > 10:
            self.__a = 100
        else:
            self.__a = 200


a1 = sample(100)
print(a1.a)
