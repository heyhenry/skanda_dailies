import tkinter as tk
import json
import os
from tkinter import ttk

characters = {}
storage_filename = 'skanda.save'

class CharInfo:
    def __init__(self, char_name, char_class, char_level):
        self.char_name = char_name
        self.char_class = char_class
        self.char_level = char_level

    # def __str__(self):
        # return self.char_name

def print_details():
    char_name = charadd_name.get()
    char_class = charadd_class.get()
    char_level = charadd_level.get()

    print(f"Name: {char_name} | Class: {char_class} | Level: {char_level}")

def json_serializer(obj):
    if isinstance(obj, CharInfo):
        return {
            'char_name': obj.char_name,
            'char_class': obj.char_class,
            'char_level': obj.char_level
        }
    return obj

def save_character():

    load_characters()

    char_name = charadd_name.get()
    char_class = charadd_class.get()
    char_level = charadd_level.get()

    characters[char_name] = CharInfo(char_name, char_class, char_level)

    json_data = json.dumps(characters, default=json_serializer, indent=4)

    with open(storage_filename, 'w') as outfile:
        outfile.write(json_data)

def load_characters():

    if os.path.exists(storage_filename):
        with open(storage_filename, 'r') as file:
            char_data = json.load(file)
            for char_name, char_info in char_data.items():
                characters[char_name] = CharInfo(char_name, char_info['char_class'], char_info['char_level'])

root = tk.Tk()
root.title('Skanda')
root.geometry('300x300')

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

home_frame = tk.Frame(notebook, bg='lightblue')
charadd_frame = tk.Frame(notebook, bg='lightyellow')
checklist_frame = tk.Frame(notebook, bg='lightgreen')

home_frame.pack()
charadd_frame.pack()
checklist_frame.pack()

notebook.add(home_frame, text='Home')
notebook.add(charadd_frame, text='Add Char')
notebook.add(checklist_frame, text='Bossing')

# home frame
home_title = tk.Label(home_frame, text='Skanda | Home')
charlst_lbl = tk.Label(home_frame, text='Character List:')
charlst_lb = tk.Listbox(home_frame)
charlst_btn = tk.Button(home_frame, text='Select Character')

home_title.grid(row=0, column=0)
charlst_lbl.grid(row=1, column=0)
charlst_lb.grid(row=2, column=0)
charlst_btn.grid(row=3, column=0)

# char add frame
charadd_title = tk.Label(charadd_frame, text='Skanda | Add Character')

charadd_name_lbl = tk.Label(charadd_frame, text='Character Name:')
charadd_name = tk.Entry(charadd_frame)

charadd_class_lbl = tk.Label(charadd_frame, text='Character Class:')
charadd_class = tk.Entry(charadd_frame)

charadd_level_lbl = tk.Label(charadd_frame, text='Character Level:')
charadd_level = tk.Entry(charadd_frame)

charadd_btn = tk.Button(charadd_frame, text='Submit', command=save_character)

charadd_title.grid(row=0, columnspan=2)
charadd_name_lbl.grid(row=1, column=0)
charadd_class_lbl.grid(row=2, column=0)
charadd_level_lbl.grid(row=3, column=0)
charadd_name.grid(row=1, column=1)
charadd_class.grid(row=2, column=1)
charadd_level.grid(row=3, column=1)
charadd_btn.grid(row=4, columnspan=2)

# checklist frame


root.mainloop()