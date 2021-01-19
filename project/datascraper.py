import requests , psycopg2

url = "https://www.jumia.com.eg/redmi-note-7-6.3-inch-64gb-dual-sim-4g-mobile-phone-neptune-blue-xiaomi-mpg166709.html"

payload={}
headers = {
  'authority': 'www.jumia.com.eg',
  'pragma': 'no-cache',
  'cache-control': 'no-cache',
  'accept': 'application/json',
  'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.jumia.com.eg/xiaomi-redmi-note-8-6.3-inch-64gb4gb-mobile-phone-space-black-15421326.html',
  'accept-language': 'en-US,en;q=0.9,ar;q=0.8',

}

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)


# def open_conn(JUMIA):
#     conn = psycopg2.connect(database="automated_price_comparison", user = "postgres", password = "dana20499", host = "127.0.0.1", port = "5432")
#     cur = conn.cursor()
#     return(conn,cur)
#     cur.execute("INSERT INTO JUMIA (ID,SKU,TITLE,MANUFACTURE,CATEGORY,KEYWORDS,EAN,ACTIVE,LASTPRICE,PRODUCT_ID,JUMIA_ID,RATE) values (%s ,%s , %s , %s, %s, %s, %s, %s, %s, %s, %s, %s)")
#     conn.commit()
#     conn.close()

# conn,cur = open_conn("TITLE")