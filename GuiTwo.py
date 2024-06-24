# Basic calculator using Tkinter in Python.
# This calculator will support basic arithmetic operations
# such as addition, subtraction, multiplication, and division.

import tkinter as tk


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


# Create the main window
root = tk.Tk()
root.title("Basic Calculator")

# Create a StringVar to hold the expression
expression = tk.StringVar()

# Create an entry box to display the expression
entry = tk.Entry(root, textvariable=expression, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for the calculator
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18), command=evaluate_expression)
    elif text == 'C':
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18), command=clear_expression)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18),
                           command=lambda t=text: update_expression(t))
    button.grid(row=row, column=col)

# Run the application
root.mainloop()
