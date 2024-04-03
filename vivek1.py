import os
import shutil
import tkinter as tk

def organize_files():
    path = path_entry.get()
    files = os.listdir(path)

    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:]

        if os.path.exists(path+'/'+extension):
            shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
        else:
            os.makedirs(path+'/'+extension)
            shutil.move(path+'/'+file, path+'/'+extension+'/')
    
    status_label.config(text="Files organized successfully!")

def button_clicked():
    print("Button clicked!")

# Create main window
root = tk.Tk()
root.title("File Organizer")

# Create and add widgets
label = tk.Label(root, text="Enter the path to organize files:")
label.pack()

path_entry = tk.Entry(root)
path_entry.pack()

organize_button = tk.Button(root, text="Organize Files", command=organize_files)
organize_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

# Run the GUI
root.mainloop()