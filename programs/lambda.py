x = lambda a, b: a * b
print(x(2, 15))



def myFunc(n):
  return lambda a : a * n

myDoubler = myFunc(2)
print(myDoubler(11))