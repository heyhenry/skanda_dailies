import json
import tkinter as tk
from tkinter import ttk

storage_filename = 'mayplesave_json'

class CharInfo:
    def __init__(self, name, char_class, level):
        self.name = name
        self.char_class = char_class
        self.level = level

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

charsub_btn = tk.Button(cdt_frame, text='Submit Character')

cdt_lbl.grid(row=0, column=0, columnspan=2)
name_lbl.grid(row=1, column=0)
name_entry.grid(row=1, column=1)
class_lbl.grid(row=2, column=0)
class_entry.grid(row=2, column=1)
level_lbl.grid(row=3, column=0)
level_entry.grid(row=3, column=1)
charsub_btn.grid(row=4, column=0, columnspan=2, pady=10)




root.mainloop()