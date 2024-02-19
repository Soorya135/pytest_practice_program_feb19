"""
#operator overloading
#method overloading/overriding
#constructor overloding and over riding
"""


# operator overloading

class operatoroverloading:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):  # operator overloading
        total = self.x + other.x
        return total


obj1 = operatoroverloading(10)
obj2 = operatoroverloading(20)
print(obj1 + obj2)

# This is an example of operator overloading also we can change the operator itself for example
# we have used self.x + other.x , instead we can use self.x - other.x

