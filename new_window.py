
from tkinter import *
from PIL import ImageTk, Image

root = Tk() # Init app
root.title("Base window") # Set title here
root.iconbitmap("Images/neon.ico") # Insert icon here
root.geometry("500x200")

my_img = None # Init empty variable for new window image.

def open():
    global my_img
    top = Toplevel() # Create new window
    top.title("New window") # Set new window title here
    top.iconbitmap("Images/neon.ico") # Insert new window icon here
    my_img = ImageTk.PhotoImage(Image.open("Images/Burger.jpg").resize((400,400))) # Define image
    my_label = Label(top, image=my_img).pack() # Put image on screen
    btn2 = Button(top, text="Close window", command=top.destroy).pack()
    
btn = Button(root, text="Open new window", command=open).pack() # Button for opening new window


root.mainloop() # Keep the app running