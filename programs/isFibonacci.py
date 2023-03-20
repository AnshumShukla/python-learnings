n = int(input("Enter the number: "))
a = b = 1
if n == 0 or n == 1:
    print("Yes")
else:
    while b < n:
        a, b = b, a + b
    if b == n:
        print("Yes")
    else:
        print("No")
