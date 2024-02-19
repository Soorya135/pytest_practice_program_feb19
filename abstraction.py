"""
example of abstraction
"""


class Test:
    a = 1
    _b = 2
    __c = 3

    def display_a(self):
        print(self.a)

    def _display_b(self):
        print(self._b)

    def __display_c(self):
        print(self.__c)

    def display_protected_method(self):
        self._display_b()

    def display_private_method(self):
        self.__display_c()

obj = Test()
obj.display_a()
# obj._display_b()
# obj._Test__display_c()

obj.display_protected_method()
obj.display_private_method()