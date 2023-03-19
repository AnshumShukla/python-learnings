a = [12, 23, 34, 45, 56, 67, 78, 89]
key = 45


def binSearch(a, key):
    l = 0
    h = len(a) - 1
    while l < h:
        mid = (l + h) // 2
        if key == a[mid]:
            return mid
        elif key > a[mid]:
            l = mid + 1
        else:
            h = mid - 1
    return -1

print(binSearch(a, key))

# complexity log(base2)n