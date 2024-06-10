import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Mayple Gearing Checklist')
root.geometry('550x500+700+200')

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

frame1 = tk.Frame(notebook, bg='#E6E6FA')
frame2 = tk.Frame(notebook, bg='#F0F8FF')

frame1.pack()
frame2.pack()

notebook.add(frame1, text='Tab 1')
notebook.add(frame2, text='Tab 2')

# frame 1 (character information input / counter)
counter = 0
completed_counter = tk.IntVar()
char_name = tk.StringVar()
current_char = tk.StringVar()

def display_name():
    global counter
    curr_name = char_name.get()
    current_char.set(curr_name)
    char_name.set('')
    counter += 1
    completed_counter.set(counter)

name_lbl = tk.Label(frame1, text="Enter Character Name: ")
name_entry = tk.Entry(frame1, textvariable=char_name, justify='center')
displayname_lbllbl = tk.Label(frame1, text="Current Character: ")
displayname_lbl = tk.Label(frame1, textvariable=current_char)
counter_lbllbl = tk.Label(frame1, text='Character Counter: ') 
counter_lbl = tk.Label(frame1, textvariable=completed_counter)
sub_btn = tk.Button(frame1, text="Submit", command=display_name)

name_lbl.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
displayname_lbllbl.grid(row=1, column=0)
displayname_lbl.grid(row=1, column=1)
counter_lbllbl.grid(row=2, column=0)
counter_lbl.grid(row=2, column=1)
sub_btn.grid(row=3, columnspan=2)

test_lbl = tk.Label(frame2, textvariable=current_char)
test_lbl.pack()


root.mainloop()
