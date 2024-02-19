class Emp:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __init__(self, name, age, salary):
    #     self.name = name
    #     self.age = age
    #     self.salary = salary

    def print(self):
        print(f"The name of the employee is {self.name}")
        print(f"The age of the employee is {self.age}")


emp1 = Emp("soorya", "25")
emp1.print()

# Note : constructor overloading is not possible, we cannot have two constructors with same name with mutilpe arguments.
