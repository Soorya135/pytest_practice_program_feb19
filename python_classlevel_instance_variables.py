# class variables

# instance variables

class Dog:
    class_dogs_legs = 4   # class level variables

    def __init__(self):
        self.name = "dog1"     # instance level variables
        self.age = 20


a1 = Dog()
a2 = Dog()

print(a1.name)
print(a2.name)

print(Dog.class_dogs_legs)