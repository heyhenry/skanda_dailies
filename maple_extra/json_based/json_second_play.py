import tkinter as tk
import json

class CharInfo:
    def __init__(self, name, race, level):
        self.name = name,
        self.race = race,
        self.level = level

root = tk.Tk()
root.title('Jsoning')
root.geometry('300x300')

name_entry = tk.Entry(root)
name_entry.insert(0, 'Enter Name')

race_entry = tk.Entry(root)
race_entry.insert(0, 'Enter Race')

level_entry = tk.Entry(root)
level_entry.insert(0, 'Enter Level')

sub_btn = tk.Button(text='Submit')

name_entry.pack()
race_entry.pack()
level_entry.pack()
sub_btn.pack()



root.mainloop()