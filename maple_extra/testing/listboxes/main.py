import tkinter as tk

class CharInfo:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name

root = tk.Tk()
root.title('listboxes')
root.geometry('300x300')

listbox = tk.Listbox(root)
listbox.pack(fill='both', expand='True')
c1 = CharInfo('henry', 25)
c2 = CharInfo('marc', 17)

listbox.insert('end', c1)
listbox.insert('end', c2)


root.mainloop()