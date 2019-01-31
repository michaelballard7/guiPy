import sqlite3

"""
- Python DB Programming:
1. Connect to a database
2. Create a cursor object
3. Write an SQL Query
"""
def create_table():
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    # pass sql to my execute function
    cursor.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()

def insert(item, quantity, price):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO store VALUES (?,?,?)",(item, quantity, price))
    connection.commit()
    connection.close()

def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    data = cur.fetchall()
    conn.close()
    return data

def update(quantity, price, item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity, price, item))
    conn.commit()
    conn.close()

def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,)) # in sqlite I must add the comma
    conn.commit()
    conn.close()

create_table()
insert("wine bottle",1,29.00)
update(11,6.0,"wine bottle")
print(view())
