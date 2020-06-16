
from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk() # Init app
root.title("Tkinter with database") # Set title here
root.iconbitmap("./../Images/neon.ico") # Insert icon here
root.geometry("500x500")

# Database

# Create or connect to database
conn = sqlite3.connect('address_book.db')

# Create connection cursor
c = conn.cursor()

# Create table
c.execute(""" CREATE TABLE addresses (
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer
        )""")

# Commit changes
conn.commit()

# Close connection
conn.close()

root.mainloop() # Keep the app running