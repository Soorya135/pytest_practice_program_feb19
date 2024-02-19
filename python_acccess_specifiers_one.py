from testpackage.acccess_specifiers import AccessSpecifiers

a1 = AccessSpecifiers()

print(a1.public_var)
print(a1._protected_var)
print(a1._AccessSpecifiers__private_var)

print(a1.public_method())
print(a1._protected_method())
print(a1._AccessSpecifiers__private_method())




