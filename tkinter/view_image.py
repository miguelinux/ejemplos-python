import tkinter as tk
from tkinter import PhotoImage

# Create the main window
parent = tk.Tk()
parent.title("Image in Tkinter")

# Load the image 
image = PhotoImage(file="../pillow/mexico.png")

# Create a label to display the image
image_label = tk.Label(parent, image=image)
image_label.pack()

# Start the Tkinter event loop
parent.mainloop()

