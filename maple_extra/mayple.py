import tkinter as tk
from tkinter import ttk

# window setup
root = tk.Tk()
root.title('Mayple Helper')
root.geometry('400x300')

# variables
char_name = tk.StringVar()
char_class = tk.StringVar()
char_level = tk.StringVar()
completed_counter = tk.IntVar()
counter = 0

# functions
def update_counter():
    global counter 
    counter += 1
    completed_counter.set(counter)

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
char_name = tk.StringVar()
char_class = tk.StringVar()
char_level = tk.StringVar()

charname_lbl = tk.Label(cdt_frame, text='Enter Character Name: ')
charname_entry = tk.Entry(cdt_frame, textvariable=char_name)
charclass_lbl = tk.Label(cdt_frame, text='Enter Character Class: ')
charclass_entry = tk.Entry(cdt_frame, textvariable=char_class)
charlevel_lbl = tk.Label(cdt_frame, text='Enter Character Level: ')
charlevel_entry = tk.Entry(cdt_frame, textvariable=char_level)

charname_lbl.grid(row=0, column=0)
charname_entry.grid(row=0, column=1)
charclass_lbl.grid(row=1, column=0)
charclass_entry.grid(row=1, column=1)
charlevel_lbl.grid(row=2, column=0)
charlevel_entry.grid(row=2, column=1)

# clt_frame (character list tab)


# sat_frame (satistical analysis tab)


root.mainloop()