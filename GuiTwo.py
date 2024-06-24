# Basic calculator using Tkinter in Python.
# This calculator will support basic arithmetic operations
# such as addition, subtraction, multiplication, and division.

import tkinter as tk
from tkinter import ttk


# Function to update the expression in the entry box
def update_expression(value):
    expression.set(expression.get() + str(value))


# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(expression.get())
        expression.set(result)
    except Exception as e:
        expression.set("Error")


# Function to clear the entry box
def clear_expression():
    expression.set("")


# Function to clear the last entry (similar to CE)
def clear_last_entry():
    expression.set(expression.get()[:-1])


# Function to close the application
def close_app():
    root.destroy()


# Create the main window
root = tk.Tk()
root.overrideredirect(True)  # Hide the title bar
root.configure(bg='#1E1E1E', bd=2, relief='solid')  # Add border to the form


# Function to center the window on the screen
def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    window.geometry(f'{window_width}x{window_height}+{x}+{y}')


# Create a custom header frame
header_frame = tk.Frame(root, bg='#1E1E1E')
header_frame.grid(row=0, column=0, columnspan=4, sticky='nsew')

# Add title to the header frame
title_label = tk.Label(header_frame, text="Calculator", bg='#1E1E1E', fg='white', font=("Arial", 14))
title_label.pack(side=tk.LEFT, padx=10, pady=5)

# Add close button to the header frame
close_button = tk.Button(header_frame, text="X", command=close_app, bg='#1E1E1E', fg='white', font=("Arial", 14),
                         relief='flat', bd=0)
close_button.pack(side=tk.RIGHT, padx=10, pady=5)

# Set the style for ttk widgets
style = ttk.Style(root)
style.theme_use('clam')

# Create a StringVar to hold the expression
expression = tk.StringVar()

# Custom style for the Entry widget
style.configure('TEntry', fieldbackground='#1E1E1E', foreground='white', borderwidth=0, relief='flat')

# Create an entry box to display the expression
entry = ttk.Entry(root, textvariable=expression, font=("Arial", 20), justify='right', style='TEntry')
entry.grid(row=1, column=0, columnspan=4, pady=10, padx=10, sticky='nsew')

# Button colors
button_bg = '#333333'
button_fg = '#FFFFFF'
operator_bg = '#444444'
operator_fg = '#FFFFFF'
equal_bg = '#C5A14B'
equal_fg = '#000000'

# Create buttons for the calculator
buttons = [
    ('%', 2, 0, button_bg, button_fg), ('CE', 2, 1, button_bg, button_fg), ('C', 2, 2, button_bg, button_fg),
    ('/', 2, 3, operator_bg, operator_fg),
    ('7', 3, 0, button_bg, button_fg), ('8', 3, 1, button_bg, button_fg), ('9', 3, 2, button_bg, button_fg),
    ('*', 3, 3, operator_bg, operator_fg),
    ('4', 4, 0, button_bg, button_fg), ('5', 4, 1, button_bg, button_fg), ('6', 4, 2, button_bg, button_fg),
    ('-', 4, 3, operator_bg, operator_fg),
    ('1', 5, 0, button_bg, button_fg), ('2', 5, 1, button_bg, button_fg), ('3', 5, 2, button_bg, button_fg),
    ('+', 5, 3, operator_bg, operator_fg),
    ('+/-', 6, 0, button_bg, button_fg), ('0', 6, 1, button_bg, button_fg), ('.', 6, 2, button_bg, button_fg),
    ('=', 6, 3, equal_bg, equal_fg)
]

# Add buttons to the window
for (text, row, col, bg, fg) in buttons:
    button = tk.Button(root, text=text, command=(
        evaluate_expression if text == '=' else clear_expression if text == 'C' else clear_last_entry if text == 'CE' else lambda
            t=text: update_expression(t)), bg=bg, fg=fg, font=("Arial", 18), relief='flat', bd=0)
    if text == '=':
        button.grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew", rowspan=2)
    else:
        button.grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

# Configure grid weights for responsive layout
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)


# Allow window dragging
def start_move(event):
    root.x = event.x
    root.y = event.y


def do_move(event):
    x = (event.x_root - root.x)
    y = (event.y_root - root.y)
    root.geometry(f"+{x}+{y}")


header_frame.bind("<ButtonPress-1>", start_move)
header_frame.bind("<B1-Motion>", do_move)

# Center the window
root.update_idletasks()
center_window(root)

# Run the application
root.mainloop()
