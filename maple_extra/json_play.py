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

chars_dict = {}

for player in chars:
    chars_dict[player.name] = [player.name, player.role, player.level]

json_data = json.dumps(chars_dict, indent=4)

with open('sample.json', 'w') as outfile:
    outfile.write(json_data)