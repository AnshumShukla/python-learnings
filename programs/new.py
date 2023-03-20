a = [10, 50, 60, 70, 80, 5, 90]


def high_marks(n):
    if n >= 60:
        return True
    else:
        return False


result = list(map(high_marks, a))

print(result)

print(type(result))
