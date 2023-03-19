def toh(n, a, b, c):
    if n > 0:
        toh(n-1, a, c, b)
        print("From "+ str(a) + " to " + str(c))
        toh(n-1, b, a, c)

n = int(input("Enter number of disks: "))

toh(n, 1, 2, 3) 

