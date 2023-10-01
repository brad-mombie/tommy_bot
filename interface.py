import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("User Interface")
root.geometry("800x480")
root.configure(bg='white')

# Create a style object
style = ttk.Style()

# Configure the custom style for the 'Okay' button
style.configure('TButton', font=('calibri', 10, 'bold'), borderwidth='4')
style.map('TButton',
          foreground=[('pressed', 'black'), ('active', 'black')],
          background=[('pressed', '!disabled', 'dark green'), ('active', 'light green')]
         )

# Create the 'Okay' button using the custom style and place it at the bottom left
okay_button = ttk.Button(root, text="Okay", command=lambda: print("Okay pressed"), style='TButton')
okay_button.place(x=10, y=430, width=100, height=40)

# Configure the custom style for the 'Why' button
style.configure('TButtonYellow', font=('calibri', 10, 'bold'), borderwidth='4')
style.map('TButtonYellow',
          foreground=[('pressed', 'black'), ('active', 'black')],
          background=[('pressed', '!disabled', 'dark orange'), ('active', 'light yellow')]
         )

# Create the 'Why' button using the custom style and place it at the bottom right
why_button = ttk.Button(root, text="Why", command=lambda: print("Why pressed"), style='TButtonYellow')
why_button.place(x=690, y=430, width=100, height=40)

root.mainloop()
