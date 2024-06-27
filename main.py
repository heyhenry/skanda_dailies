import tkinter as tk
import json
import os

root = tk.Tk()
root.title('Skanda')
root.geometry('300x300')

home_frame = tk.Frame(root, bg='lightblue')
home_frame.pack()

home_title = tk.Label(home_frame, text='Skanda | Home Page')
home_title.pack()

root.mainloop()