import tkinter as tk


def on_button_click():
    label.config(text="Hello, Tkinter!")


# Create the main window
root = tk.Tk()
root.title("Tkinter Example")

# Create a label
label = tk.Label(root, text="Welcome to Tkinter!")
label.pack(pady=10)

# Create a button
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=5)

# Run the application
root.mainloop()
