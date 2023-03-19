ages = [20, 21, 19, 18]


def myFunc(x):
    if x > 19:
        return False
    else:
        return True


adults = filter(myFunc, ages)

for x in adults:
    print(x)

