import tkinter as tk
from tkinter import ttk
import json

class CharInfo:
    def __init__(self, name, char_class, level):
        self.name = name
        self.char_class = char_class
        self.level = level

    def print_info(self):
        print(f"Character Name: {self.name}\nCharacter Class: {self.char_class}\nCharacter Level: {self.level}")

# window setup
root = tk.Tk()
root.title('Mayple Helper')
root.geometry('400x300')

# variables
completed_counter = tk.IntVar()
counter = 0

# functions
def update_counter():
    global counter 
    counter += 1
    completed_counter.set(counter)

def submit_charinfo():
    char_name = charname_entry.get()
    char_class = charclass_entry.get()
    char_level = charlevel_entry.get()

    char_obj = CharInfo(char_name, char_class, char_level)

# notebook (tab system) setup
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

cdt_frame = tk.Frame(notebook, bg='lightblue')

clt_frame = tk.Frame(notebook, bg='lightgreen')
sat_frame = tk.Frame(notebook, bg='lightyellow')

cdt_frame.pack()
clt_frame.pack()
sat_frame.pack()

notebook.add(cdt_frame, text='CDT')
notebook.add(clt_frame, text='CLT')
notebook.add(sat_frame, text='SAT')

# cdt_frame (character details tab)

cdt_lbl = tk.Label(cdt_frame, text="Character Details")
charname_lbl = tk.Label(cdt_frame, text='Enter Character Name: ')
charname_entry = tk.Entry(cdt_frame)
charclass_lbl = tk.Label(cdt_frame, text='Enter Character Class: ')
charclass_entry = tk.Entry(cdt_frame)
charlevel_lbl = tk.Label(cdt_frame, text='Enter Character Level: ')
charlevel_entry = tk.Entry(cdt_frame)
charsub_btn = tk.Button(cdt_frame, text='Submit Character', command=submit_charinfo)

cdt_lbl.grid(row=0, column=0, columnspan=2)
charname_lbl.grid(row=1, column=0)
charname_entry.grid(row=1, column=1)
charclass_lbl.grid(row=2, column=0)
charclass_entry.grid(row=2, column=1)
charlevel_lbl.grid(row=3, column=0)
charlevel_entry.grid(row=3, column=1)
charsub_btn.grid(row=4, column=0, columnspan=2)

# clt_frame (character list tab)


# sat_frame (satistical analysis tab)


root.mainloop()