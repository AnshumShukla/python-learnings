def letterCount(name, c):
    f = open( name, "r")
    text = f.read()
    print(text.count(c))

name = input("Enter file name ")
c = input("Enter the character you wanna search for ")
letterCount(name, c)