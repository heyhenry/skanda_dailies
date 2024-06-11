import tkinter as tk
import json

json_filename = 'jsoning.json'

class CharInfo:
    def __init__(self, name, race, level):
        self.name = name
        self.race = race
        self.level = level

root = tk.Tk()
root.title('Jsoning')
root.geometry('300x300')

characters = {}

def json_serializer(obj):
    if isinstance(obj, CharInfo):
        return {
            'char_name': obj.name,
            'char_race': obj.race,
            'char_level': obj.level
        }
    return obj

def save_characters():
    char_name = name_entry.get()
    char_race = race_entry.get()
    char_level = level_entry.get()
    
    characters[char_name] = CharInfo(char_name, char_race, char_level)
    
    json_data = json.dumps(characters, default=json_serializer, indent=4)
    
    with open(json_filename, 'w') as outfile:
        outfile.write(json_data)

name_entry = tk.Entry(root)
name_entry.insert(0, 'Enter Name')

race_entry = tk.Entry(root)
race_entry.insert(0, 'Enter Race')

level_entry = tk.Entry(root)
level_entry.insert(0, 'Enter Level')

sub_btn = tk.Button(text='Submit', command=save_characters)

name_entry.pack()
race_entry.pack()
level_entry.pack()
sub_btn.pack()


root.mainloop()