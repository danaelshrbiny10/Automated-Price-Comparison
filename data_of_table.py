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
#    print ("SKU = "), row[1]
#    print ("NAME = "), row[2]
#    print ("CATEGORIES = "), row[4]
#    print ("PRICES = "), row[8]
#    print ("rating = "), row[11], "\n"

# cur.execute("SELECT * from PRICE_HISTORY")
# rows = cur.fetchall()
# for row in rows:
#    print ("PRICES = "), row[0], "\n"

# cur.execute("SELECT * from CATEGORY")
# rows = cur.fetchall()
# for row in rows:
#    print ("NAME = "), row[0]
#    print ("url = "), row[1], "\n"

conn.commit()
print ("Operation done successfully");
conn.close()
