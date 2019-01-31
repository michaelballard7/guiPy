import psycopg2 as pg

"""
- Python DB Programming:
1. Connect to a database
2. Create a cursor object
3. Write an SQL Query
"""

params = "dbname='store' user='postgres' password='root' port='5432'"


def create_table():
    connection = pg.connect(params)
    cursor = connection.cursor()
    # pass sql to my execute function
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS inventory(item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()


def insert(item, quantity, price):
    connection = pg.connect(params)
    cursor = connection.cursor()
    # cursor.execute("INSERT INTO inventory VALUES ('%s','%s','%s')"%(item, quantity, price))  # this is vulnerable to an sqlInjection
    cursor.execute("INSERT INTO inventory VALUES (%s,%s,%s)", (item, quantity, price))
    connection.commit()
    connection.close()


def view():
    conn = pg.connect(params)
    cur = conn.cursor()
    cur.execute("SELECT * FROM inventory")
    data = cur.fetchall()
    conn.close()
    return data


def update(quantity, price, item):
    conn = pg.connect(params)
    cur = conn.cursor()
    cur.execute("UPDATE inventory SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()


def delete(item):
    conn = pg.connect(params)
    cur = conn.cursor()
    # in sqlite I must add the comma
    cur.execute("DELETE FROM inventory WHERE item=%s", (item,))
    conn.commit()
    conn.close()


create_table()
insert("Corona", 1, 3.00)
# update(11, 6.0, "wine bottle")
print(view())
