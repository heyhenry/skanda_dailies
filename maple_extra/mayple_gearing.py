import tkinter as tk


root = tk.Tk()
root.title('Mayple Gearing Checklist')
root.geometry('400x300')

char_name = tk.StringVar()
display_name = tk.StringVar()

def update_display():
    name = char_name.get()
    display_name.set(name)

name_lbl = tk.Label(root, text='Character Name: ').pack()
name_entry = tk.Entry(root, textvariable=char_name).pack()
namesub_btn = tk.Button(root, text='submit', command=update_display).pack()

display_lbl = tk.Label(root, textvariable=display_name).pack()

root.mainloop()
