# Modules
import sqlite3
from Project_Data import l_prod
from Project_Data import l_ord
import csv


# Loop on Menu options until finished
def f_menu():
    print(
        """
        Menu
        1 - Connect to Database
        2 - Create a Product table
        3 - Create a Order table
        4 - Create a Date table
        5 - Load Products
        6 - Load Orders
        7 - Load Dates
        8 - Create View for product order
        9 - Create View for order
        10 - Update Price
        11 - Display
        12 - Display View for product order
        13 - Display View for order
        14 - Close Database Connection
        X - Exit
        """)
    choice = input("choice:")
    # while choice.upper() != 'X':
    return choice

def f_db_connect():

    db_conn = ""
    db_name = "MedProdPy.db"
    stat = True

    try:
        db_conn = sqlite3.connect(db_name)        # Get database connection object
        db_conn.execute("PRAGMA foreign_keys = ON;")
        print (db_name, "Connected")
    except Exception as e:
        print("Error connection to : " + str(e))  # Print error message
        stat = False

    return db_conn, stat

def f_pr_tb_create():

    stat = True
    sql = ""

    try:
        sql = "DROP TABLE IF EXISTS products;"
        g_db_conn.execute(sql)
        sql = '''CREATE TABLE products 
             (id INTEGER PRIMARY KEY AUTOINCREMENT ,
              prod_nbr   TEXT NOT NULL UNIQUE ,
              prod_line  TEXT NOT NULL,
              size       TEXT NOT NULL,
              color      TEXT NOT NULL,
              price      REAL NOT NULL CHECK(TYPEOF(price) == 'real' AND price > 5.0)
             );
                '''
        g_db_conn.execute(sql)
        print("Table created")

    except Exception as e:
        print("Error disconnection: " + str(e))  # Print error message
        stat = False

    return stat

def f_or_tb_create():

    stat  = True

    try:
        sql = "DROP TABLE IF EXISTS orders;"
        g_db_conn.execute(sql)

        sql = '''CREATE TABLE orders
             (id       INTEGER PRIMARY KEY AUTOINCREMENT,
              ord_nbr  INTEGER NOT NULL UNIQUE,
              prod_id  INTEGER NOT NULL,
              ord_qty  INTEGER NOT NULL CHECK(TYPEOF(ord_qty) == 'integer'),
              ord_date TEXT    NOT NULL,
              FOREIGN KEY(prod_id) REFERENCES products(id) ON DELETE CASCADE
             );
             '''
        g_db_conn.execute(sql)

        sql = "CREATE INDEX IF NOT EXISTS orders_prod_id_fk on orders (prod_id);"
        g_db_conn.execute(sql)
        print("Order table Created")

    except Exception as e:
        print("Error disconnection: " + str(e))  # Print error message
        stat = False

    return stat

def f_date_tb_create():

    stat  = True

    try:
        sql = "DROP TABLE IF EXISTS dates;"
        g_db_conn.execute(sql)

        sql = '''CREATE TABLE dates
        (id INTEGER PRIMARY KEY AUTOINCREMENT ,
        date       TEXT UNIQUE  ,
        day        TEXT NOT NULL,
        month      TEXT NOT NULL
        );
        '''

        g_db_conn.execute(sql)

        sql = "CREATE INDEX IF NOT EXISTS order_ord_date_idx on orders (ord_date);"
        g_db_conn.execute(sql)
        print("Date table Created")

    except Exception as e:
        print("Error disconnection: " + str(e))  # Print error message
        stat = False

    return stat

def f_load_products():

    stat = True
    sql = ""
    csr = g_db_conn.cursor()
    insert = 0

    try:
        for i in l_prod:
            g_db_conn.execute('BEGIN TRANSACTION')

            try:
                sql = "SELECT id FROM products WHERE prod_nbr = ?;"
                csr.execute(sql, (i[0],))
                row = csr.fetchone()


                if row == None:
                    sql = "INSERT INTO products (prod_nbr, prod_line, size, color, price) VALUES (?,?,?,?,?);"
                    csr.execute(sql, (i[0], i[1], i[2], i[3], i[4]))
                    insert += 1

                else:
                    print("Product already exist")

                g_db_conn.commit()

            except Exception as e:
                print("Error update product number: ", i[0] + str(e))  # Print error message
                g_db_conn.rollback()

        # Commit product table transactions
        g_db_conn.commit()
        print(insert,"rows of product loaded")

    except Exception as e:
        print("Product loading fail " + str(e))  # Print error message
        g_db_conn.rollback()
        stat = False

    return stat

def f_load_orders():

    stat = True
    sql = ""
    csr = g_db_conn.cursor()
    insert = 0

    try:
        for i in l_ord:
            g_db_conn.execute('BEGIN TRANSACTION')

            try:
                sql = "SELECT id FROM orders WHERE ord_nbr = ?;"
                csr.execute(sql, (i[0],))
                row = csr.fetchone()


                if row != None:
                    print("Order number", i([0]), "exist")
                    g_db_conn.commit()
                    insert += 1
                    continue


                sql = "SELECT id FROM products WHERE prod_nbr = ?;"
                csr.execute(sql, (i[1],))
                row = csr.fetchone()


                if row == None:
                    print("Product number", str(i[1]), "not exist")
                    g_db_conn.commit()
                    insert += 1
                    continue

                sql = "SELECT id FROM products WHERE prod_nbr = ?;"
                csr.execute(sql, (i[1],))
                row = csr.fetchone()
                for num in row:
                    sql = "INSERT INTO orders (ord_nbr, prod_id, ord_qty, ord_date) VALUES (?,?,?,?);"
                    g_db_conn.execute(sql, (i[0], num, i[2], i[3]))
                    g_db_conn.commit()
                    insert += 1

            except Exception as e:
                print("Error update order number: ", i[1], str(e))  # Print error message
                g_db_conn.rollback()

        g_db_conn.commit()
        print(insert, "rows of orders updated")

    except Exception as e:
        print("Order update fail " + str(e))  # Print error message
        stat = False

    return stat

def f_load_dates():

    stat = True

    try:
        g_db_conn.execute('BEGIN TRANSACTION')

        sql = '''INSERT INTO dates (date, day, month)
        SELECT DISTINCT ord_date, strftime('%w',ord_date), strftime('%m',ord_date)
        FROM orders
        WHERE ord_date NOT IN (SELECT date FROM dates);
        '''
        g_db_conn.execute(sql)
        g_db_conn.commit()

    except Exception as e:
        print("Date update fail " + str(e))  # Print error message
        g_db_conn.rollback()
        stat = False

    return stat

def f_v_prod_ord():

    stat = True
    sql = ""

    try:
        sql = "DROP VIEW IF EXISTS v_prod_ord;"
        g_db_conn.execute(sql)
        sql = '''  CREATE VIEW IF NOT EXISTS v_prod_ord AS
            SELECT
            P.prod_nbr, P.prod_line, P.color, P.size, P.price,
            CASE WHEN O.ord_nbr IS NULL THEN 0 ELSE O.ord_nbr END AS ord_nbr,
            CASE WHEN O.ord_nbr IS NULL THEN 0 ELSE 1         END AS ord_cnt,
            CASE WHEN O.ord_qty IS NULL THEN 0 ELSE O.ord_qty END AS ord_qty,
            P.price * ifnull( O.ord_qty, 0) AS ord_amt
            FROM products P LEFT OUTER JOIN orders O ON P.id = O.prod_id;
            '''
        g_db_conn.execute(sql)
        print("View for product order created")

    except Exception as e:
        print("Error create the view for product order : " + str(e))  # Print error message
        stat = False

    return stat

def f_v_ord():

    stat = True
    sql = ""

    try:
        sql = "DROP VIEW IF EXISTS v_ord;"
        g_db_conn.execute(sql)
        sql = '''CREATE VIEW IF NOT EXISTS v_ord AS
            SELECT P.prod_nbr, P.price,
                O.ord_qty,
                P.price * ifnull(O.ord_qty, 0) AS ord_amt,
                D.date, D.month,
                CASE D.day WHEN '0' THEN 'SUNDAY' 
                    WHEN '1' THEN 'MONDAY'
                    WHEN '2' THEN 'TUESDAY'
                    WHEN '3' THEN 'WEDNESDAY'
                    WHEN '4' THEN 'THURSDAY'
                    WHEN '5' THEN 'FRIDAY'
                    WHEN '6' THEN 'SATURDAY'
                    ELSE 'OTHER' END AS day_name
            FROM products P
                INNER JOIN orders O ON P.id       = O.prod_id
                INNER JOIN dates  D ON O.ord_date = D.date;
            '''
        g_db_conn.execute(sql)
        print("View for orders created")

    except Exception as e:
        print("Error create the view for orders: " + str(e))  # Print error message
        stat = False

    return stat

def f_update_price():

    stat = True
    sql = ""
    csr = g_db_conn.cursor()

    try:
        for i in l_prod:
            try:
                sql = "SELECT id FROM products WHERE prod_nbr = ?;"
                csr.execute(sql, (i[0],))
                row = csr.fetchone()

                if row == None:
                    sql = "INSERT INTO products (prod_nbr, prod_line, size, color, price) VALUES (?,?,?,?,?);"
                    csr.execute(sql, (i[0], i[1], i[2], i[3], i[4]))

                else:
                    sql = "UPDATE products SET price = ? WHERE id = ?;"
                    csr.execute(sql, (i[4], row[0]))

                g_db_conn.commit()

            except Exception as e:
                print("Error update product number: ", i[0] + str(e))  # Print error message

        g_db_conn.commit()
        print("Products updated")

    except Exception as e:
        print("Product update fail " + str(e))  # Print error message
        stat = False

    return stat


def f_display():

    stat = True
    sql = ""
    csr = g_db_conn.cursor()

    try:
        sql = "SELECT * FROM products"
        csr.execute(sql)
        for row in csr.fetchall():
            print(row)
    except Exception as e:
        print("Error select all from products: " + str(e))  # Print error message
        stat = False

    return stat

def f_d_v_prod_ord():

    stat = True
    sql = ""
    csr = g_db_conn.cursor()

    hdr_fmt = "|{0:^14}|{1:^9}|{2:^9}|{3:^12}|{4:^14}|{5:^14}|{6:^14}|"  # Header format
    dat_fmt = "|{0:<14}|{1:<9}|{2:<9}|{3:<12}|{4:<14}|{5:<14}|{6:<14}|"  # Data   format

    # Display the report header
    print(hdr_fmt.format('--------------', '---------', '---------', '------------', '--------------', '--------------', '--------------'))  # Header data
    print(hdr_fmt.format('Product Number', 'Size', 'Color', 'Sales Price', 'Order Count', 'Order Quantity', 'Total Sales $'))  # Header data
    print(hdr_fmt.format('--------------', '---------', '---------', '------------', '--------------', '--------------', '--------------'))  # Header data

    try:
        sql = """SELECT * FROM v_prod_ord
            GROUP BY ord_nbr
            ORDER BY sum(ord_amt) DESC;
            """
        csr.execute(sql)
        for row in csr.fetchall():
            print(dat_fmt.format(row[0], row[3], row[2], row[4], row[6], row[7], row[8]))
    except Exception as e:
        print("Error select all from v_prod_ord: " + str(e))  # Print error message
        stat = False

    return stat

def f_d_v_ord():

    stat = True
    sql = ""
    csr = g_db_conn.cursor()

    hdr_fmt = "|{0:^14}|{1:^14}|"  # Header format
    dat_fmt = "|{0:<14}|{1:<14}|"  # Data   format

    # Display the report header
    print(hdr_fmt.format('--------------', '--------------'))  # Header data
    print(hdr_fmt.format('Date', 'Total Sales $'))  # Header data
    print(hdr_fmt.format('--------------', '--------------'))  # Header data

    try:
        sql = """SELECT * FROM v_ord
            GROUP BY date
            ORDER BY date ASC;
            """
        csr.execute(sql)
        for row in csr.fetchall():
            print(dat_fmt.format(row[4], row[3]))
    except Exception as e:
        print("Error select all from v_ord: " + str(e))  # Print error message
        stat = False

    return stat

def f_db_disconnect():

    stat = True

    try:
        g_db_conn.close()
        print("Database Disconnected")
    except Exception as e:
        print("Error disconnection: " + str(e))  # Print error message
        stat = False

    return stat



#################################################################



def main():
    global g_db_conn
    choice = ""
    status = True

    while choice not in ["x", "X"]:
        choice = f_menu()

        # Conditional Branching based on Menu choice
        # Exit
        if choice.upper() == "X":
            print("Good-bye.")

        # Connect to database
        elif choice == "1":
            print("Connect to Database")
            g_db_conn, status = f_db_connect()
            if not status : choice = "X"

        #Create a new table
        elif choice == "2":
            print("Create a new table")
            status = f_pr_tb_create()
            if not status : choice = "X"

        #Create a Order table
        elif choice == "3":
            print("Create a Order table")
            status = f_or_tb_create()
            if not status : choice = "X"

        #Create a Date table
        elif choice == "4":
            print("Create a Date table")
            status = f_date_tb_create()
            if not status : choice = "X"

        #Load Products
        elif choice == "5":
            print("Loading products")
            status = f_load_products()
            if not status : choice = "X"

        #Load Orders
        elif choice == "6":
            print("Loading orders")
            status = f_load_orders()
            if not status : choice = "X"

        #Load Dates
        elif choice == "7":
            print("Loading dates")
            status = f_load_dates()
            if not status : choice = "X"

        #Create View for product order
        elif choice == "8":
            print("Create product order view")
            status = f_v_prod_ord()
            if not status : choice = "X"

        #Create View for orders
        elif choice == "9":
            print("Create order view")
            status = f_v_ord()
            if not status : choice = "X"

        # Update the Price
        elif choice == "10":
            print("Price updated")
            status = f_update_price()
            if not status : choice = "X"

        # Display the Table
        elif choice == "11":
            print("Data display")
            status = f_display()
            if not status : choice = "X"

        # Display View for product order
        elif choice == "12":
            print("Data display View for product order")
            status = f_d_v_prod_ord()
            if not status : choice = "X"

        # Display tView for orders
        elif choice == "13":
            print("Data display View for orders")
            status = f_d_v_ord()
            if not status : choice = "X"

        # Close the database
        elif choice == "14":
            print("Disconnect to Database")
            status = f_db_disconnect()
            if not status : choice = "X"

        # some unknown choice
        else:
            print("Sorry, but", choice, "isn't a valid choice.")

    input("\n\nPress the enter key to exit.")
    return


# run main()
main()
