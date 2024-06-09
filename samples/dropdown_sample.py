import tkinter as tk

# sample code provided by: https://www.tutorialsfreak.com/python-tutorial/drop-down-menus-in-python-tkinter

def on_option_select(event):
    selected_option.set(event)

root = tk.Tk()
root.title("Dropdown Menu Example")
root.geometry("400x300")

# create a string var to hold the selected option
selected_option = tk.StringVar()

# create the dropdown menu
options = ["Option 1", "Option 2", "Option 3", "Option 4"]
dropdown = tk.OptionMenu(root, selected_option, *options)
dropdown.pack(pady=10)

# add a button to display the selected option
show_button = tk.Button(root, text="Show Selection", command=lambda: on_option_select(selected_option.get()))
show_button.pack()

# label to display the selected option
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()