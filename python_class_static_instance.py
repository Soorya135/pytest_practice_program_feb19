"""
There are 3 types of methods static, class and instance methods.
"""


class Dog:
    class_dogs_legs = 4  # class level variables

    def __init__(self):
        self.name = "dog1"  # instance level variables
        self.age = 20

    def get_dog(self):
        print(self.name)
        print(self.age)

    @classmethod
    def get_legs(cls):
        print(cls.class_dogs_legs)

    @staticmethod
    def get_name_age():
        print(Dog.class_dogs_legs)


obj = Dog()
obj.get_dog()
Dog.get_legs()
Dog.get_name_age()
