class Test:

    def __init__(self):
        print("Inside constructor Parent")

    def add(self):
        print("parent add")

class student(Test):

    def __init__(self):
        super().__init__()
        print("Inside constructor child")

    def add(self):
        super().add()
        print("child add")

obj1 = student()
obj1.add()
