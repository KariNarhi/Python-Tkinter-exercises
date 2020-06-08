
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk() # Init app
root.title("Base window") # Set title here
root.iconbitmap("Images/neon.ico") # Insert icon here
root.geometry("500x500")

my_image = None

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/Dev/Python/Python-Tkinter-exercises/Images", title="Select a file", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename).resize((400,400)))
    my_image_label = Label(image=my_image).pack()

my_btn = Button(root, text="Open file", command=open).pack()

root.mainloop() # Keep the app running