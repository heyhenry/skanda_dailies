import json

class CharInfo:
    def __init__(self, name, role, level):
        self.name = name
        self.role = role
        self.level = level

obj1 = CharInfo('Henry', 'Mage', 21)
obj2 = CharInfo('Jeo', 'Warrior', 22)
obj3 = CharInfo('Mas', 'knight', 22)

chars = [obj1, obj2, obj3]

chars_dict = {}

for char in chars:
    chars_dict[char.name] = char

def custom_json_serializer(obj):
    if isinstance(obj, CharInfo):
        return {
            'name': obj.name,
            'role': obj.role,
            'level': obj.level
        }
    return obj

json_data = json.dumps(chars_dict, default=custom_json_serializer, indent=4)

with open('sample.json', 'w') as outfile:
    outfile.write(json_data)
