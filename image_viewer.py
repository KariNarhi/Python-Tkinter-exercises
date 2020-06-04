
from tkinter import *
from PIL import ImageTk, Image

root = Tk() # Init app
root.title("Images") # Set title here
root.iconbitmap("Images/neon.ico") # Insert icon here

my_img1 = ImageTk.PhotoImage(Image.open("Images/Burger.jpg").resize((400,400))) # Insert image here
my_img2 = ImageTk.PhotoImage(Image.open("Images/Burger2.jpg").resize((400,400))) # Insert image here
my_img3 = ImageTk.PhotoImage(Image.open("Images/Burger3.jpg").resize((400,400))) # Insert image here

image_list = [my_img1, my_img2, my_img3] # List of images

my_label = Label(image=my_img1) # Define image into label
my_label.grid(row=0, column=0, columnspan=3) # Place image on the screen

###### Define button logic ######

def forward(image_number):
    global my_label
    global button_back
    global button_forward

    my_label.grid_forget() # Delete previous image from view
    my_label = Label(image=image_list[image_number-1]) # Change image number

    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1)) # Re-define forward button
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))       # Re-define back button

    if image_number == 3:
        button_forward = Button(root, text=">>", state=DISABLED) # Disable forward if last image

    # Place buttons and image on screen again
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3)

def back(image_number):
    global my_label
    global button_back
    global button_forward

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])

    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED) # Disable back if first image

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3)

###### End button logic ######

button_back = Button(root, text="<<", command=lambda: back, state=DISABLED) # Define back button
button_exit = Button(root, text="Exit Program", command=root.quit)          # Define exit button
button_forward = Button(root, text=">>", command=lambda: forward(2))        # Define forward button

# Place buttons on the screen
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop() # Keep the app running