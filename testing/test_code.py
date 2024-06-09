import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Testing")
root.geometry("400x300")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

frame1 = tk.Frame(notebook, background="blue")
frame2 = tk.Frame(notebook, background="green")
frame3 = tk.Frame(notebook, background="black")

frame1.pack()
frame2.pack()
frame3.pack()

notebook.add(frame1, text="Tab 1")
notebook.add(frame2, text="Tab 2")
notebook.add(frame3, text="Tab 3")

root.mainloop()