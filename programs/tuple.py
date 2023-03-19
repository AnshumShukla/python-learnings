import random

tup = ('anshum', 'azeem', 'vishal')
print(tup)

x = list(tup)
x[2] = "pranav"
tup = tuple(x)
print(tup)

if "anshum" in tup:
    print("Present")