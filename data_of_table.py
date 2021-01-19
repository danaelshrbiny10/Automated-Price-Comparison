import psycopg2 

def open_conn(n1 , n2 , n3 ,n4 ,n5):
    conn = psycopg2.connect(database="automated_price_comparison", user = "postgres", password = "dana20499", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    return(conn,cur)
    cur.execute("INSERT INTO JUMIA (SKU,NAME,CATEGORIES,PRICES,rating) values (%s ,%s , %s , %s, %s)")
    conn.commit()
    conn.close()

conn,cur = open_conn("SKU","NAME" , "CATEGORIES","PRICES","rating")
#---------------------------------------------------------------------------------------------------------------------------------------------
def open_conn(n):
    conn = psycopg2.connect(database="automated_price_comparison", user = "postgres", password = "dana20499", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    return(conn,cur)
    cur.execute("INSERT INTO PRICE_HISTORY (PRICES) values (%s)")
    conn.commit()
    conn.close()

conn,cur = open_conn("PRICES")
#---------------------------------------------------------------------------------------------------------------------------------------------
def open_conn(x1 , x2):
    conn = psycopg2.connect(database="automated_price_comparison", user = "postgres", password = "dana20499", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    return(conn,cur)
    cur.execute("INSERT INTO  category (NAME , url) values (%s ,%s)" )
    conn.commit()
    conn.close()

conn,cur = open_conn("NAME" , "url")

#---------------------------------------------------------------------------------------------------------------------------------------------

## to show tables
# cur = conn.cursor()
# cur.execute("SELECT *  from JUMIA")
# rows = cur.fetchall()
# for row in rows:
#    print ("ID = "), row[0]
#    print ("SKU = "), row[1]
#    print ("TITLE = "), row[2]
#    print ("MANUFACTURE = "), row[3]
#    print ("CATEGORY = "), row[4]
#    print ("KEYWORDS = "), row[5]
#    print ("EAN = "), row[6]
#    print ("ACTIVE = "), row[7]
#    print ("LASTPRICE = "), row[8]
#    print ("PRODUCT_ID = "), row[9]
#    print ("JUMIA_ID = "), row[10]
#    print ("RATE = "), row[11], "\n"

# cur.execute("SELECT * from PRICE_HISTORY")
# rows = cur.fetchall()
# for row in rows:
#    print ("PRODUCT_ID = "), row[0]
#    print ("DATE = "), row[1]
#    print ("PRICE = "), row[2], "\n"

# cur.execute("SELECT * from CATEGORY")
# rows = cur.fetchall()
# for row in rows:
#    print ("NAME = "), row[0]
#    print ("url = "), row[1], "\n"

conn.commit()
print ("Operation done successfully");
conn.close()
