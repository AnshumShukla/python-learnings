def average(n):
    l = list(n)
    try:
        avg = sum(l)/len(l)
        print(avg)
    except ZeroDivisionError:
        print(0.0)
    else:
        print("No exception raised")
    finally:
        print("ye phir aa gya")

average([12, 23, 45, 65, 67, 87])
print("\n")
average([])