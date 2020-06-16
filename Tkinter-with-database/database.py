
from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk() # Init app
root.title("Tkinter with database") # Set title here
root.iconbitmap("./../Images/neon.ico") # Insert icon here
root.geometry("350x400")

# Database

# Create or connect to database
conn = sqlite3.connect('address_book.db')

# Create connection cursor
c = conn.cursor()

# Create table (commented out)
''' c.execute(""" CREATE TABLE addresses (
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer
        )""") '''

# Create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# Text box labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text="ID to delete")
delete_box_label.grid(row=9, column=0, pady=5)

# Submit function
def submit():

    # Connect to database
    conn = sqlite3.connect('address_book.db')
    # Create connection cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
            {
                'f_name' : f_name.get(),
                'l_name' : l_name.get(),
                'address' : address.get(),
                'city' : city.get(),
                'state' : state.get(),
                'zipcode' : zipcode.get()
            })

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

    # Clear textboxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Submit button
submit_btn = Button(root, text="Add record to database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_label = None

# Query function
def query():

    # Connect to database
    conn = sqlite3.connect('address_book.db')
    # Create connection cursor
    c = conn.cursor()

    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    # print(records)

    # Loop results
    print_records = "  Name \t\t ID \n\n" 
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + "\t" + str(record[6]) + "\n"
        print("\n" + str(record))

    global query_label
    query_label = Label(root, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

# Query button
query_btn = Button(root, text="Get records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=130)

# Delete function
def delete():
    # Connect to database
    conn = sqlite3.connect('address_book.db')
    # Create connection cursor
    c = conn.cursor()

    c.execute("DELETE FROM addresses WHERE oid=" + delete_box.get())

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

    # Clear Delete ID entry
    delete_box.delete(0, END)

    # Clear query results label
    query_label.grid_forget()

# Delete button
delete_btn = Button(root, text="Delete record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

# Commit changes
conn.commit()

# Close connection
conn.close()

root.mainloop() # Keep the app running