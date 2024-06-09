import tkinter as tk

# sample code provided by: https://www.tutorialsfreak.com/python-tutorial/drop-down-menus-in-python-tkinter

def on_option_select(event):
    selected_option.set(event)
    display_size.set(event)

root = tk.Tk()
root.title("Dropdown Menu Example")
root.geometry("400x300")

# create a string var to hold the selected option
selected_option = tk.IntVar(value="Select Party Size")
display_size = tk.IntVar()

# create the dropdown menu
options = [1, 2, 3, 4, 5, 6]
dropdown = tk.OptionMenu(root, selected_option, *options)
dropdown.pack(pady=10)

# add a button to display the selected option
show_button = tk.Button(root, text="Show Selection", command=lambda: on_option_select(selected_option.get()))
show_button.pack()

# label to display the selected option
result_label = tk.Label(root, textvariable=display_size)
result_label.pack()

root.mainloop()