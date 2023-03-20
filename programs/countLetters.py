def countLetters(str):
    upper, lower, other = 0, 0, 0
    for i in range(len(str)):
        if str[i].isupper():
            upper += 1
        elif str[i].islower():
            lower += 1
        else:
            other += 1
        
    print("Upper letters:", upper)
    print("Lower letters:", lower)
    print("Other letters:", other)

str = "Hi my name is Pranav"
countLetters(str)