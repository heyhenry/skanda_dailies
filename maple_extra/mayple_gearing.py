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

root.mainloop()
