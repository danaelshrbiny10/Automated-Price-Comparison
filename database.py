import psycopg2

conn = psycopg2.connect(database="automated_price_comparison", user = "postgres", password = "dana20499", host = "127.0.0.1", port = "5432")

print ("Opened database successfully")



cur = conn.cursor()

cur.execute('''CREATE TABLE SOUQ
      (ID INT PRIMARY KEY     NOT NULL,
      SKU VARCHAR(50),
      TITLE VARCHAR(300),
      MANUFACTURE VARCHAR(50),
      DESCRIPTION TEXT    NOT NULL,
      ImG TEXT    NOT NULL,
      CATEGORY INT     NOT NULL,
      KEYWORDS TEXT    NOT NULL,
      EAN VARCHAR(50),
      ACTIVE BOOLEAN,
      LASTPRICE VARCHAR(50),
      PRODUCT_ID VARCHAR(50),
      SOUQ_ID INT     NOT NULL,
      RATE INT     NOT NULL)''');


cur.execute('''CREATE TABLE JUMIA
      (ID INT PRIMARY KEY     NOT NULL,
      SKU VARCHAR(50),
      TITLE VARCHAR(300),
      MANUFACTURE VARCHAR(50),
      CATEGORY INT     NOT NULL,
      KEYWORDS TEXT    NOT NULL,
      EAN VARCHAR(50),
      ACTIVE BOOLEAN,
      LASTPRICE VARCHAR(50),
      PRODUCT_ID VARCHAR(50),
      JUMIA_ID INT     NOT NULL,
      RATE INT     NOT NULL)''');

cur.execute('''CREATE TABLE NOON
      (ID INT PRIMARY KEY     NOT NULL,
      SKU VARCHAR(50),
      TITLE VARCHAR(300),
      MANUFACTURE VARCHAR(50),
      CATEGORY INT     NOT NULL,
      KEYWORDS TEXT    NOT NULL,
      EAN VARCHAR(50),
      ACTIVE BOOLEAN,
      LASTPRICE VARCHAR(50),
      PRODUCT_ID VARCHAR(50),
      NOON_ID INT     NOT NULL,
      RATE INT     NOT NULL)''');



cur.execute('''CREATE TABLE PRODUCT
      (ID INT PRIMARY KEY     NOT NULL,
      SKU VARCHAR(50),
      TITLE VARCHAR(300),
      MANUFACTURE VARCHAR(50),
      DESCRIPTION TEXT    NOT NULL,
      CATEGORY INT     NOT NULL,
      KEYWORDS TEXT    NOT NULL,
      EAN VARCHAR(50),
      LOWPRICE VARCHAR(50),
      AVG_RATE INT     NOT NULL)''');


cur.execute('''CREATE TABLE PRICE_HISTORY
      (PRODUCT_ID INT PRIMARY KEY     NOT NULL,
      DATE DATE,
      PRICE VARCHAR(50))''');

cur.execute('''CREATE TABLE CATEGORY
      (NAME VARCHAR(300),
      url VARCHAR (500))''');

cur.execute('''CREATE TABLE IMG
      (ID INT PRIMARY KEY     NOT NULL,
      PRODUCT_ID INT     NOT NULL,
      IMG_PATH VARCHAR(50))''');

cur.execute('''CREATE TABLE CUSTOMER
      (ID INT PRIMARY KEY     NOT NULL,
      FIRSTNAME VARCHAR(50),
      LASTNAME VARCHAR(50),
      EMAIL VARCHAR(100),
      PASSWORD VARCHAR(300))''');

cur.execute('''CREATE TABLE NOTIFY
      (ID INT PRIMARY KEY     NOT NULL,
      CUSTOMER_ID INT     NOT NULL,
      PRODECT_ID INT     NOT NULL,
      IM_PRICE VARCHAR(100),
      ENDED BOOLEAN )''');

print ("Table created successfully")

conn.commit()
conn.close()