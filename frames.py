from tkinter import *

root = Tk() # Init app
root.title("Frames") # Set title here
root.iconbitmap("Images/neon.ico") # Insert icon here

# Define frame
frame = LabelFrame(root, text="This is a frame", padx=50, pady=50)
frame.pack(padx=10, pady=10)

# Define buttons
button1 = Button(frame, text="Click Here!")
button1.grid(row=0, column=0, padx=10)

button2 = Button(frame, text="...and here!")
button2.grid(row=0, column=1, padx=10)

root.mainloop() # Keep the app running