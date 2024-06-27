import tkinter as tk
import json
import os
from tkinter import ttk



def print_details():
    char_name = charadd_name.get()
    char_class = charadd_class.get()
    char_level = charadd_level.get()

    print(f"Name: {char_name} | Class: {char_class} | Level: {char_level}")


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
home_title.pack()

# char add frame
charadd_title = tk.Label(charadd_frame, text='Skanda | Add Character')

charadd_name_lbl = tk.Label(charadd_frame, text='Character Name:')
charadd_name = tk.Entry(charadd_frame)

charadd_class_lbl = tk.Label(charadd_frame, text='Character Class:')
charadd_class = tk.Entry(charadd_frame)

charadd_level_lbl = tk.Label(charadd_frame, text='Character Level:')
charadd_level = tk.Entry(charadd_frame)

charadd_btn = tk.Button(charadd_frame, text='Submit', command=print_details)

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