a = [12, 23, 34, 45, 56, 67, 78, 89]
key = 45


def binSearch(a, key, l, h):
    while l < h:
        mid = (l + h) // 2
        if key == a[mid]:
            return mid
        elif key > a[mid]:
            return (a, key, mid+1, h)
        else:
            return (a, key, l, mid-1)
    return -1


print(binSearch(a, key, 0, len(a)-1))
