import tkinter as tk

def submit_name():
    name = name_input.get()
    print("Entered name:", name)
    # do something with the entered name, e.g. start the game with the name

# create the dialog box
dialog = tk.Tk()
dialog.title("Enter Your Name")

# add the input field
name_label = tk.Label(dialog, text="Name:")
name_label.pack(side=tk.LEFT)
name_input = tk.Entry(dialog)
name_input.pack(side=tk.LEFT)

# add the submit button
submit_button = tk.Button(dialog, text="Submit", command=submit_name)
submit_button.pack(side=tk.RIGHT)

# start the dialog box
dialog.mainloop()