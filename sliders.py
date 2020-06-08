
from tkinter import *

root = Tk() # Init app
root.title("Slider") # Set title here
root.iconbitmap("Images/neon.ico") # Insert icon here
root.geometry("500x500")

vertical = Scale(root, from_=0, to=500) # Vertical slider
vertical.pack()

def slide():
    my_label1 = Label(root, text= "\n" + "Horizontal: " + str(horizontal.get())).pack() # show horizontal value
    my_label2 = Label(root, text="Vertical: " + str(vertical.get())).pack() # show vertical value
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get())) # Resize window based on slider values

horizontal = Scale(root, from_=0, to=500, orient=HORIZONTAL) # Horizontal slider
horizontal.pack()

my_btn = Button(root, text="Click here!", command=slide).pack() # Button for resizing window and showing new horizontal value.

root.mainloop() # Keep the app running