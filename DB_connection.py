import psycopg2

conn = psycopg2.connect(database="automated_price_comparison", user = "postgres", password = "pass123", host = "127.0.0.1", port = "5432")

print ("Opened database successfully")