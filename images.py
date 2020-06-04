
from tkinter import *
from PIL import ImageTk, Image

root = Tk() # Init app
root.title("Images") # Set title here
root.iconbitmap("Images/neon.ico") # Insert icon here

my_img = ImageTk.PhotoImage(Image.open("Images/Burger.jpg").resize((300,400))) # Insert image here
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop() # Keep the app running