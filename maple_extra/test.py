import tkinter as tk

root = tk.Tk()

# Create labels and place them in a grid layout
label1 = tk.Label(root, text="Label 1")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Label 2")
label2.grid(row=0, column=1)

label3 = tk.Label(root, text="Label 3")
label3.grid(row=1, column=0)

label4 = tk.Label(root, text="Label 4")
label4.grid(row=1, column=1)

# Configure all rows and columns to be resizable
for i in range(2):  # assuming 2 rows and columns
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()


