
from tkinter import *

root = Tk() # Init app
root.title("Dropdown") # Set title here
root.iconbitmap("Images/neon.ico") # Insert icon here
root.geometry("500x500")

def show():
    myLabel = Label(root, text=clicked.get()).pack() # Show selected value

# Values to be selected
options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

clicked = StringVar()
clicked.set(options[0]) # Set initial value

drop = OptionMenu(root, clicked, *options) # Dropdown menu
drop.pack()

myButton = Button(root, text="Show selection", command=show).pack() # Button for showing value

root.mainloop() # Keep the app running