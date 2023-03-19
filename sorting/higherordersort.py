def secondElement(t):
    return t[1]


z = [('Guitar', 'Jimmy'), ('Vocals', 'Robert'),
     ('Bass', 'John Paul'), ('Drums', 'John')]

print(sorted(z))

print(sorted(z, key=secondElement))