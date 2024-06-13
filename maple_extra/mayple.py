import json
import os
import tkinter as tk
from tkinter import ttk

storage_filename = 'mayplesave.json'
characters = {}

# character object 
class CharInfo:
    def __init__(self, name, char_class, level):
        self.name = name
        self.char_class = char_class
        self.level = level

# custom json serializer
def json_serializer(obj):
    if isinstance(obj, CharInfo):
        return {
            'char_name': obj.name,
            'char_class': obj.char_class,
            'char_level': obj.level
        }
    return obj

# save new characters to save file
def save_characters():

    load_characters()

    char_name = name_entry.get()
    char_class = class_entry.get()
    char_level = level_entry.get()

    characters[char_name] = CharInfo(char_name, char_class, char_level)

    json_data = json.dumps(characters, default=json_serializer, indent=4)

    with open(storage_filename, 'w') as outfile:
        outfile.write(json_data)

# load all character data from save file
def load_characters():

    if os.path.exists(storage_filename): 

        with open(storage_filename, 'r') as file:
            char_data = json.load(file)
            for char_name, char_info in char_data.items():
                characters[char_name] = CharInfo(char_name, char_info['char_class'], char_info['char_level'])

# insert all character names into check list (listbox)
def populate_checklist():

    load_characters()
    
    for char_name in characters:
        char_lb.insert('end', char_name)

# initial window setup
root = tk.Tk()
root.title("Mayple Gearing")
root.geometry("300x300")

# creating tab system
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

cdt_frame = tk.Frame(notebook, bg='lightblue')
clt_frame = tk.Frame(notebook, bg='lightgreen')
sat_frame = tk.Frame(notebook, bg='lightyellow')

cdt_frame.pack()
clt_frame.pack()
sat_frame.pack()

notebook.add(cdt_frame, text='Character Details')
notebook.add(clt_frame, text='Check List')
notebook.add(sat_frame, text='Statistic Analysis')

# character details tab
cdt_lbl = tk.Label(cdt_frame, text='Character Details', bg='lightblue')

name_lbl = tk.Label(cdt_frame, text='Enter Name:', bg='lightblue')
name_entry = tk.Entry(cdt_frame)

class_lbl = tk.Label(cdt_frame, text='Enter Class:', bg='lightblue')
class_entry = tk.Entry(cdt_frame)

level_lbl = tk.Label(cdt_frame, text='Enter Character Level:', bg='lightblue')
level_entry = tk.Entry(cdt_frame)

charsub_btn = tk.Button(cdt_frame, text='Submit Character', command=save_characters)

cdt_lbl.grid(row=0, column=0, columnspan=2)
name_lbl.grid(row=1, column=0)
name_entry.grid(row=1, column=1)
class_lbl.grid(row=2, column=0)
class_entry.grid(row=2, column=1)
level_lbl.grid(row=3, column=0)
level_entry.grid(row=3, column=1)
charsub_btn.grid(row=4, column=0, columnspan=2, pady=10)

# character check list tab
clt_lbl = tk.Label(clt_frame, text='Character Check List', bg='lightgreen')
clt_lbl.pack()
char_lb = tk.Listbox(clt_frame)
char_lb.pack(fill='both', expand=True)
populate_checklist()

root.mainloop()