def makePairs(a, b):
    x = list(a)
    y = list(b)

    if len(x) != len(y):
        print("Not possible! Enter equal length lists.")

    c = []
    for i in range(len(x)):
        tup = (x[i], y[i])
        c.append(tup)

    print(c)


makePairs([1, 3, 5, 7], [2, 4, 6, 8])
makePairs([], [])
