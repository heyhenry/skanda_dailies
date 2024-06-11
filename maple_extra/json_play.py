import json

class CharInfo:
    def __init__(self, name, role, level):
        self.name = name
        self.role = role
        self.level = level

obj1 = CharInfo('Henry', 'Mage', 21)
obj2 = CharInfo('Jeo', 'Warrior', 22)
obj3 = CharInfo('Mas', 'knight', 22)

chars = []
chars.append(obj1)
chars.append(obj2)
chars.append(obj3)

for i in chars:
    print("========")
    print(i.name)
    print(i.role)
    print(i.level)
    print("========")