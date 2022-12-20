import os
import tkinter as tk
from tkinter import filedialog, Checkbutton
import datetime

# Function to bulk rename files
def rename_files():
# Get the directory containing the files
    directory = filedialog.askdirectory()

# Get the prefix to add to the file names
    prefix = prefix_entry.get()

# Get the value of the checkbox
    add_date = date_checkbox.get()

# Get the list of files in the directory
    file_list = os.listdir(directory)

# Counter for the number to add to the file name
    i = 1

# Loop through the list of files
    for file in file_list:
# Get the file name and extension
        file_name, file_extension = os.path.splitext(file)

# Create the new file name
        new_name = prefix + str(i)

# Add the date to the file name if the checkbox is checked
        if add_date:
            current_date = datetime.datetime.now().strftime("%m%Y")
            new_name += "_" + current_date

# Add the extension back to the new file name
        new_name += file_extension

# Rename the file
        os.rename(os.path.join(directory, file), os.path.join(directory, new_name))

# Increment the counter
        i += 1

# Create the main window
window = tk.Tk()
window.title("Bulk Rename")

# Create a label for the prefix entry
prefix_label = tk.Label(text="Enter a prefix for the file names:")
prefix_label.pack()

# Create a text entry for the prefix
prefix_entry = tk.Entry()
prefix_entry.pack()

# Create a checkbox for adding the date to the file name
date_checkbox = tk.BooleanVar()
add_date_checkbox = Checkbutton(text="Add date to file name", variable=date_checkbox)
add_date_checkbox.pack()

# Create a button to run the rename function
rename_button = tk.Button(text="Rename files", command=rename_files)
rename_button.pack()

# Start the main loop
window.mainloop()
