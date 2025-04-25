import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
parent = tk.Tk()
parent.title("Image in Tkinter")

# Load and display an image 
image = Image.open("../pillow/mexico.png")
image = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = tk.Label(parent, image=image)
image_label.pack()

# Start the Tkinter event loop
parent.mainloop()

