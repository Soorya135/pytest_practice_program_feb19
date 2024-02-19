"""
Method overloading
"""


class A:

    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


obj1 = A()
# print(obj1.add(10, 20))
print(obj1.add(10, 20, 30))

# Here we have same add function with different number of arguments, but python will consider only the last function
# Method overloading is not possible in python
# Constructor overloading is not possible in python
# pythn will take the last one writen in the memory

