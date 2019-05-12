import psycopg2


def create_table():
    # you must first create a database in postgre
    # provide database name, username, password, host, and port number
    conn = psycopg2.connect("dbname='Postgre_demo' user='postgres' password='postgres' host='localhost' port='5432'")
    # create a cursor object
    cursor = conn.cursor()
    # create a table "store" if it doesnt exist yet
    # define columns in table (column_name data_format, column_name data_format...)
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    # save changes and close database connection
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    """adds a new item to the table"""
    conn = psycopg2.connect("dbname='Postgre_demo' user='postgres' password='postgres' host='localhost' port='5432'")
    cursor = conn.cursor()
    # insert the values into the specified table
    # INSERT INTO table_name VALUES(value, value, value...)
    cursor.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()


def read():
    """gets and prints all items currently in the table"""
    conn = psycopg2.connect("dbname='Postgre_demo' user='postgres' password='postgres' host='localhost' port='5432'")
    cursor = conn.cursor()
    # select all values present in specified table
    cursor.execute("SELECT * FROM store")
    # return python list with corresponding table data
    rows = cursor.fetchall()
    conn.close()
    return rows


def delete_item(item_name):
    """deletes an item from the table"""
    conn = psycopg2.connect("dbname='Postgre_demo' user='postgres' password='postgres' host='localhost' port='5432'")
    cursor = conn.cursor()
    # specify table to delete from when row item name matches provided name
    # adda comma after single entry as tuples cannot be formed if only (item_name) is provided
    cursor.execute("DELETE FROM store WHERE item=%s", (item_name,))
    conn.commit()
    conn.close()


def edit_item(item, quantity, price):
    """updates the values of an item in the table"""
    conn = psycopg2.connect("dbname='Postgre_demo' user='postgres' password='postgres' host='localhost' port='5432'")
    cursor = conn.cursor()
    # specify table to update, new values to set and what row new values should affect
    cursor.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()


create_table()
insert("Short Mug", 1, 100)
insert("Mean Mug", 5,  60)
insert("Sexy Mug", 9, 999)
#delete_item("Short Mug")
#edit_item("Mean Mug", 8, 90)
print(read())
