import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os


# Function to list files in the selected directory
def list_files(directory):
    for widget in file_list_frame.winfo_children():
        widget.destroy()

    try:
        files = os.listdir(directory)
        for file in files:
            file_label = tk.Label(file_list_frame, text=file, bg='#1E1E1E', fg='white', anchor='w')
            file_label.pack(fill='x')
    except Exception as e:
        error_label = tk.Label(file_list_frame, text=str(e), bg='#1E1E1E', fg='red')
        error_label.pack()


# Function to open a directory dialog
def open_directory():
    directory = filedialog.askdirectory()
    if directory:
        list_files(directory)


# Create the main window
root = tk.Tk()
root.title("Windows Explorer")
root.geometry("800x600")
root.configure(bg='#1E1E1E')

# Create a custom header frame
header_frame = tk.Frame(root, bg='#1E1E1E', bd=2, relief='solid')
header_frame.pack(side='top', fill='x')

# Add title to the header frame
title_label = tk.Label(header_frame, text="Windows Explorer", bg='#1E1E1E', fg='white', font=("Arial", 14))
title_label.pack(side=tk.LEFT, padx=10, pady=5)

# Add open directory button to the header frame
open_button = tk.Button(header_frame, text="Open", command=open_directory, bg='#1E1E1E', fg='white', font=("Arial", 14),
                        relief='flat', bd=0)
open_button.pack(side=tk.RIGHT, padx=10, pady=5)

# Create the navigation panel
nav_panel = tk.Frame(root, bg='#1E1E1E', width=200, bd=2, relief='solid')
nav_panel.pack(side='left', fill='y')

# Create the file list frame
file_list_frame = tk.Frame(root, bg='#1E1E1E', bd=2, relief='solid')
file_list_frame.pack(side='right', fill='both', expand=True)

# Sample directories in the navigation panel
directories = ['Documents', 'Downloads', 'Pictures', 'Music', 'Videos']
for dir in directories:
    dir_label = tk.Label(nav_panel, text=dir, bg='#1E1E1E', fg='white', anchor='w')
    dir_label.pack(fill='x', padx=10, pady=2)
    dir_label.bind("<Button-1>", lambda e, dir=dir: list_files(os.path.expanduser(f'~/{dir}')))


# Center the window on the screen
def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    window.geometry(f'{window_width}x{window_height}+{x}+{y}')


# Center the window
center_window(root)

# Run the application
root.mainloop()
