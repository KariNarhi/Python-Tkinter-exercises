
from tkinter import *
from tkinter import messagebox

root = Tk() # Init app
root.title("Messagebox") # Set title here
root.iconbitmap("Images/neon.ico") # Insert icon here

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askyesno("This is popup", "Hello World!") # Show messagebox and get response
    if response == 1:
        Label(root, text="You clicked Yes!").pack()
    else:
        Label(root, text="You clicked No!").pack()

Button(root, text="Pop-up", command=popup).pack()


root.mainloop() # Keep the app running