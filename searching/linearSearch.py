a = [10, 43, 23, 65, 7, 99]

target = int(input("Enter the value you wanna search: "))

for i in range(len(a)):
    if target == a[i]:
        print("found at " + str(i))
        break
    else:
        print("not found")

# complexity n