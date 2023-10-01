# import tkinter as tk
# from tkinter import ttk
# import signal

# # Handler to close the tkinter window when receiving a SIGINT or SIGTERM
# def signal_handler(signum, frame):
#     root.quit()

# # Bind the signal handler
# signal.signal(signal.SIGINT, signal_handler)
# signal.signal(signal.SIGTERM, signal_handler)

# # Create the main window
# root = tk.Tk()
# root.title("User Interface")
# root.geometry("800x480")
# root.configure(bg='white')

# # Make the program run in full screen
# root.attributes("-fullscreen", True)

# # Create a style object
# style = ttk.Style()

# # Configure the custom style for the 'Okay' button with further increased font size
# style.configure('Green.TButton', 
#                 font=('calibri', 80, 'bold'), 
#                 borderwidth='4', 
#                 background='light green')
# style.map('Green.TButton',
#           foreground=[('pressed', 'black'), ('active', 'black')],
#           background=[('pressed', '!disabled', 'dark green'), ('active', 'light green')]
#          )

# # Create the 'Okay' button using the custom style and place it at the bottom left with the specified size
# okay_button = ttk.Button(root, text="Okay", command=lambda: print("Okay pressed"), style='Green.TButton')
# okay_button.place(x=100, y=200, width=800, height=320)

# # Configure the custom style for the 'Why' button with further increased font size
# style.configure('Yellow.TButton', 
#                 font=('calibri', 80, 'bold'), 
#                 borderwidth='4', 
#                 background='light yellow')
# style.map('Yellow.TButton',
#           foreground=[('pressed', 'black'), ('active', 'black')],
#           background=[('pressed', '!disabled', 'dark orange'), ('active', 'light yellow')]
#          )

# # Create the 'Why' button using the custom style and place it at the bottom right with the specified size
# why_button = ttk.Button(root, text="Why", command=lambda: print("Why pressed"), style='Yellow.TButton')
# why_button.place(x=20, y=200, width=800, height=320)

# # Add the 'sub_heading' label at the top left
# sub_heading = tk.Label(root, text="Time for your medication: ", font=('calibri', 20, 'bold'), bg='white')
# sub_heading.place(x=10, y=10)

# # Add the '[MEDICATION]' label to the left of the 'sub_heading' label
# medication_label = tk.Label(root, text="[MEDICATION]", font=('calibri', 20, 'bold'), bg='white')
# medication_label.place(x=10, y=50)

# root.mainloop()
import tkinter as tk
from tkinter import ttk
import signal

# Handler to close the tkinter window when receiving a SIGINT or SIGTERM
def signal_handler(signum, frame):
    root.quit()

# Bind the signal handler
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# Create the main window
root = tk.Tk()
root.title("User Interface")
root.geometry("800x480")
root.configure(bg='white')

# Make the program run in full screen
root.attributes("-fullscreen", True)

# Create a style object
style = ttk.Style()

# Configure the custom style for the 'Okay' button
style.configure('Green.TButton', 
                font=('calibri', 80, 'bold'), 
                borderwidth='4', 
                background='light green')
style.map('Green.TButton',
          foreground=[('pressed', 'black'), ('active', 'black')],
          background=[('pressed', '!disabled', 'dark green'), ('active', 'light green')]
         )

# Create the 'Okay' button using the custom style and place it at the bottom left
okay_button = ttk.Button(root, text="Okay", command=lambda: print("Okay pressed"), style='Green.TButton')
okay_button.place(x=20, y=660, width=800, height=320)

# Configure the custom style for the 'Why' button
style.configure('Yellow.TButton', 
                font=('calibri', 80, 'bold'), 
                borderwidth='4', 
                background='light yellow')
style.map('Yellow.TButton',
          foreground=[('pressed', 'black'), ('active', 'black')],
          background=[('pressed', '!disabled', 'dark orange'), ('active', 'light yellow')]
         )

# Create the 'Why' button using the custom style and place it at the bottom right
why_button = ttk.Button(root, text="Why", command=lambda: print("Why pressed"), style='Yellow.TButton')
why_button.place(x=5000, y=660, width=800, height=320)

# Add the 'sub_heading' label at the top left
sub_heading = tk.Label(root, text="Time for your medication: ", font=('calibri', 20, 'bold'), bg='white')
sub_heading.place(x=10, y=10)

# Add the '[MEDICATION]' label to the left of the 'sub_heading' label
medication_label = tk.Label(root, text="[MEDICATION]", font=('calibri', 20, 'bold'), bg='white')
medication_label.place(x=10, y=50)

root.mainloop()
