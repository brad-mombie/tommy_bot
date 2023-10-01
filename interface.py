import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("User Interface")
root.geometry("800x480")
root.configure(bg='white')

# Create the 'Okay' button and place it at the bottom left
okay_button = ttk.Button(root, text="Okay", command=lambda: print("Okay pressed"), background='green')
okay_button.place(x=10, y=430, width=100, height=40)

# Create the 'Why' button and place it at the bottom right
why_button = ttk.Button(root, text="Why", command=lambda: print("Why pressed"), background='yellow')
why_button.place(x=690, y=430, width=100, height=40)

root.mainloop()
