
from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk() # Init app
root.title("Tkinter with database") # Set title here
root.iconbitmap("./../Images/neon.ico") # Insert icon here
root.geometry("350x500")

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

select_box = Entry(root, width=30)
select_box.grid(row=9, column=1, pady=5)

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

select_box_label = Label(root, text="ID to select")
select_box_label.grid(row=9, column=0, pady=5)



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
        print("\n" + str(record)) # Print records on the console

    global query_label
    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

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

    c.execute("DELETE FROM addresses WHERE oid=" + select_box.get())

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

    # Clear Delete ID entry
    select_box.delete(0, END)

    # Clear query results label
    query_label.grid_forget()

# Delete button
delete_btn = Button(root, text="Delete record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=125)


# Update function
def update():
    # Connect to database
    conn = sqlite3.connect('address_book.db')
    # Create connection cursor
    c = conn.cursor()

    # Update data of the selected record ID
    record_id = str(select_box.get())

    c.execute("""UPDATE addresses SET 
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode

        WHERE oid = :oid""",
        {
            'first' : f_name_update.get(),
            'last' : l_name_update.get(),
            'address' : address_update.get(),
            'city' : city_update.get(),
            'state' : state_update.get(),
            'zipcode' : zipcode_update.get(),
            'oid': record_id
        })

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

    update_window.destroy()

# Editor function
def editor():
    global update_window # Make update window global so that it can be destroyed inside update()-function
    update_window = Tk() # Init app
    update_window.title("Update a database record") # Set title here
    update_window.iconbitmap("./../Images/neon.ico") # Insert icon here
    update_window.geometry("305x200")

    # Connect to database
    conn = sqlite3.connect('address_book.db')
    # Create connection cursor
    c = conn.cursor()

    # Get data of the selected record ID
    record_id = str(select_box.get())
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    results = c.fetchall()

    # Make update text boxes global
    global f_name_update
    global l_name_update
    global address_update
    global city_update
    global state_update
    global zipcode_update

    # Create text boxes (update window)
    f_name_update = Entry(update_window, width=30)
    f_name_update.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_update = Entry(update_window, width=30)
    l_name_update.grid(row=1, column=1)

    address_update = Entry(update_window, width=30)
    address_update.grid(row=2, column=1)

    city_update = Entry(update_window, width=30)
    city_update.grid(row=3, column=1)

    state_update = Entry(update_window, width=30)
    state_update.grid(row=4, column=1)

    zipcode_update = Entry(update_window, width=30)
    zipcode_update.grid(row=5, column=1)

    # Text box labels (update window)
    f_name_update_label = Label(update_window, text="First Name")
    f_name_update_label.grid(row=0, column=0, pady=(10, 0))

    l_name_update_label = Label(update_window, text="Last Name")
    l_name_update_label.grid(row=1, column=0)

    address_update_label = Label(update_window, text="Address")
    address_update_label.grid(row=2, column=0)

    city_update_label = Label(update_window, text="City")
    city_update_label.grid(row=3, column=0)

    state_update_label = Label(update_window, text="State")
    state_update_label.grid(row=4, column=0)

    zipcode_update_label = Label(update_window, text="Zipcode")
    zipcode_update_label.grid(row=5, column=0)

    # Insert query results 
    for data in results:
        f_name_update.insert(0, data[0])
        l_name_update.insert(0, data[1])
        address_update.insert(0, data[2])
        city_update.insert(0, data[3])
        state_update.insert(0, data[4])
        zipcode_update.insert(0, data[5])
    
    # Save button
    save_btn = Button(update_window, text="Save", command=update)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=115)
    

# Update button
update_editor_btn = Button(root, text="Update record", command=editor)
update_editor_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=125)


# Commit changes
conn.commit()

# Close connection
conn.close()

root.mainloop() # Keep the app running