class Animalparent():
    def ap(self):
        print("Inside animal parent classs")


class Animal(Animalparent):
    name = "test"

    def a(self):
        print("Inside animal classs")


class Mamal(Animal):
    def b(self):
        print("Inside mamal classs")


# mam = Mamal()
# mam.b()

# now i will introduce inheritance to mamal class

mam = Mamal()
mam.b()
mam.a()
print(mam.name)
mam.ap()

# suppose as part of doing multiple inheritance if we same function defined int he 2 classes ,method will b
# chosen based on the MRO(Method Resolution Order)
