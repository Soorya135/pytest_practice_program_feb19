"""
Test programs
"""

x = lambda x: x ** 3
print(x)

# below is the example of list comprehensions

x = [x * 2 for x in range(10)]
print(x)
x = [x * 2 for x in range(10) if x % 2 == 0]
print(x)
x = [x * 2 if x % 2 == 0 else x ** 3 for x in range(10)]
print(x)

# below is the example of dictionary comprehensions

d1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7}
d2 = {k: v ** 2 for (k, v) in d1.items()}
print(d2)
d3 = {k: v ** 2 for (k, v) in d1.items() if v % 2 == 0}
print(d2)
d4 = {k: v ** 2 if v % 2 == 0 else v ** 3 for (k, v) in d1.items()}
print(d3)
d4 = {k: v ** 2 if v % 2 == 0 else v ** 3 for (k, v) in d1.items()}
print(d4)
dic_even = {k: True if v % 2 == 0 else False for (k, v) in d1.items()}
print(dic_even)

# set comprehensions

a = {x for x in range(10)}