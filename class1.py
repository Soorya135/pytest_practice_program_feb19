class Test:
    a = 10
    b = 20

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_a(self):
        print(self.a)

    def print_b(self):
        print(self.b)


obj1 = Test(10, 20)
obj2 = Test(30, 40)

obj1.print_a()
obj1.print_b()
obj2.print_a()
obj2.print_b()

#dont use print(obj1.print_a())
