class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("Hello my name is", self.name)

p1 = Person("Pranav", 20)
p1.intro()