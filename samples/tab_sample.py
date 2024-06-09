import tkinter as tk
from tkinter import ttk

# sample code provided by YT: NeuralNine (https://www.youtube.com/watch?v=wVJyeIo2W0I)

def main():
    root = tk.Tk()
    root.title('Tab Application')
    root.geometry('400x200')

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill='both')

    frame1 = tk.Frame(notebook, width=400, height=200)
    frame2 = tk.Frame(notebook, width=400, height=200)
    frame3 = ttk.Frame(notebook, width=400, height=200)

    frame1.pack()
    frame2.pack()
    frame3.pack()

    notebook.add(frame1, text='Tab 1')
    notebook.add(frame2, text='Tab 2')
    notebook.add(frame3, text='Tab 3')

    root.mainloop()

if __name__ == "__main__":
    main()