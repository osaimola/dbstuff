import sqlite3


def create_database():
    # create connection to database if it exists or create new database
    conn = sqlite3.connect(r"C:\Users\Osa's\Desktop\UDEMY PRojcts\data.db")
    # create a cursor object
    cursor = conn.cursor()
    # create a table "store" if it doesnt exist yet
    # define columns in table (column_name data_format, column_name data_format...)
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    # save changes and close database connection
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = sqlite3.connect(r"C:\Users\Osa's\Desktop\UDEMY PRojcts\data.db")
    cursor = conn.cursor()
    # insert the values into the specified table
    # INSERT INTO table_name VALUES(value, value, value...)
    cursor.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()


def read():
    conn = sqlite3.connect(r"C:\Users\Osa's\Desktop\UDEMY PRojcts\data.db")
    cursor = conn.cursor()
    # select all values present in specified table
    cursor.execute("SELECT * FROM store")
    # return python list with corresponding table data
    rows = cursor.fetchall()
    conn.close()
    return rows


def delete_item(item_name):
    conn = sqlite3.connect(r"C:\Users\Osa's\Desktop\UDEMY PRojcts\data.db")
    cursor = conn.cursor()
    # specify table to delete from when row item name matches provided name
    # adda comma after single entry as tuples cannot be formed if only (item_name) is provided
    cursor.execute("DELETE FROM store WHERE item=?", (item_name,))
    conn.commit()
    conn.close()


def edit_item(item, quantity, price):
    conn = sqlite3.connect(r"C:\Users\Osa's\Desktop\UDEMY PRojcts\data.db")
    cursor = conn.cursor()
    # specify table to update, new values to set and what row new values should affect
    cursor.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
    conn.commit()
    conn.close()


delete_item("Short Mug")
edit_item("Mean Mug", 8, 90)
print(read())
