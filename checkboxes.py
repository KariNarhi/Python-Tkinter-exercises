
from tkinter import *

root = Tk() # Init app
root.title("Checkbox") # Set title here
root.iconbitmap("Images/neon.ico") # Insert icon here
root.geometry("300x300")

def show():
    myLabel = Label(root, text=var.get()).pack() # Show selected value

var = StringVar()

c = Checkbutton(root, text="Check this box", variable=var, onvalue="On", offvalue="Off") # Define checkbox
c.deselect() # Initialize as non-selected
c.pack()


myButton = Button(root, text="Show selection", command=show).pack() # Button for showing selected value


root.mainloop() # Keep the app running