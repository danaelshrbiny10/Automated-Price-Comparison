import psycopg2
import json

conn = psycopg2.connect(database="automated_price_comparison", user = "postgres", password = "dana20499", host = "127.0.0.1", port = "5432")

print ("Opened database successfully")


cur = conn.cursor()

cur.execute("INSERT INTO JUMIA (ID,SKU,TITLE,MANUFACTURE,DESCRIPTION,ImG,CATEGORY,KEYWORDS,EAN,ACTIVE,LASTPRICE,PRODUCT_ID,SOUQ_ID,RATE) \
    VALUES ()");

cur.execute("INSERT INTO PRODUCT (ID,SKU,TITLE,MANUFACTURE,DESCRIPTION,CATEGORY,KEYWORDS,EAN,LOWPRICE,AVG_RATE) \
    VALUES ()");

cur.execute("INSERT INTO PRICE_HISTORY (PRODUCT_ID,DATE,PRICE) \
    VALUES ()");

cur.execute("INSERT INTO CATEGORY (ID,NAME) \
    VALUES (4 , 'Phones & Tablets/Mobile Phones/Smartphones/Android Phones' )");


conn.commit()
print ("Records created successfully");
conn.close()

'''
cur = conn.cursor()
cur.execute("SELECT ID,SKU,TITLE,MANUFACTURE,DESCRIPTION,ImG,CATEGORY,KEYWORDS,EAN,ACTIVE,LASTPRICE,PRODUCT_ID,SOUQ_ID,RATE  from JUMIA")
rows = cur.fetchall()
for row in rows:
   print ("ID = "), row[0]
   print ("SKU = "), row[1]
   print ("TITLE = "), row[2]
   print ("MANUFACTURE = "), row[3]
   print ("DESCRIPTION = "), row[4]
   print ("ImG = "), row[5]
   print ("CATEGORY = "), row[6]
   print ("KEYWORDS = "), row[7]
   print ("EAN = "), row[8]
   print ("ACTIVE = "), row[9]
   print ("LASTPRICE = "), row[10]
   print ("PRODUCT_ID = "), row[11]
   print ("SOUQ_ID = "), row[12]
   print ("RATE = "), row[13], "\n"

   cur.execute("SELECT PRODUCT_ID,DATE,PRICE  from PRICE_HISTORY")
rows = cur.fetchall()
for row in rows:
   print ("PRODUCT_ID = "), row[0]
   print ("DATE = "), row[1]
   print ("PRICE = "), row[2], "\n"

cur.execute("SELECT ID,NAME from CATEGORY")
rows = cur.fetchall()
for row in rows:
   print ("ID = "), row[0]
   print ("NAME = "), row[1], "\n"


conn.commit()
print ("Operation done successfully");
conn.close()
'''