import os
import tkinter as tk
from tkinter import filedialog, Checkbutton

# function to bulk rename files
def rename_files():
    # get the directory containing the files
    directory = filedialog.askdirectory()

    # get the prefix to add to the file names
    prefix = prefix_entry.get()

    # get the value of the checkbox
    add_date = date_checkbox.get()

    # get the list of files in the directory
    file_list = os.listdir(directory)

    # counter for the number to add to the file name
    i = 1

    # loop through the list of files
    for file in file_list:
        # get the file name and extension
        file_name, file_extension = os.path.splitext(file)

        # create the new file name
        new_name = prefix + str(i)

        # add the date to the file name if the checkbox is checked
        if add_date:
            current_date = datetime.datetime.now().strftime("%m%Y")
            new_name += "_" + current_date

        # add the extension back to the new file name
        new_name += file_extension

        # rename the file
        os.rename(os.path.join(directory, file), os.path.join(directory, new_name))

        # increment the counter
        i += 1

# create the main window
window = tk.Tk()
window.title("Bulk Rename")

# create a label for the prefix entry
prefix_label = tk.Label(text="Enter a prefix for the file names:")
prefix_label.pack()

# create a text entry for the prefix
prefix_entry = tk.Entry()
prefix_entry.pack()

# create a checkbox for adding the date to the file name
date_checkbox = tk.BooleanVar()
add_date_checkbox = Checkbutton(text="Add date to file name", variable=date_checkbox)
add_date_checkbox.pack()

# create a button to run the rename function
rename_button = tk.Button(text="Rename files", command=rename_files)
rename_button.pack()

# start the main loop
window.mainloop()
