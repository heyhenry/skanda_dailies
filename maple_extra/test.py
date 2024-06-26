# import tkinter as tk

# root = tk.Tk()

# # Create labels and place them in a grid layout
# label1 = tk.Label(root, text="Label 1")
# label1.grid(row=0, column=0)

# label2 = tk.Label(root, text="Label 2")
# label2.grid(row=0, column=1)

# label3 = tk.Label(root, text="Label 3")
# label3.grid(row=1, column=0)

# label4 = tk.Label(root, text="Label 4")
# label4.grid(row=1, column=1)

# # Configure all rows and columns to be resizable
# for i in range(2):  # assuming 2 rows and columns
#     root.grid_rowconfigure(i, weight=1)
#     root.grid_columnconfigure(i, weight=1)

# root.mainloop()


# class test:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def get_name(self):
#         return self.name
    
#     def get_age(self):
#         return self.age
    
#     def set_name(self, x):
#         self.name = x

#     def set_age(self, x):
#         self.age = x

#     def print_details(self):
#         print(self.name)
#         print(self.age)

# obj = test('Henry', 2)
# obj.print_details()

# import os
# filename = 'water.json'

# check_file = os.path.isfile(filename)
# print(check_file)

# list box selection
import tkinter as tk

root = tk.Tk()
root.title('w/e')
root.geometry('300x300')

lb = tk.Listbox(root, selectmode='single')

lb.insert(1, 'Apple')
lb.insert(2, 'Banana')
lb.insert(3, 'Orange')

def selected_item():
    print(lb.curselection())

btn = tk.Button(root,text='Print Selected', command=selected_item)

btn.pack(side='bottom')
lb.pack()

root.mainloop()