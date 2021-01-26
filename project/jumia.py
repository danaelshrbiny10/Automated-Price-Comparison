import requests, psycopg2 , json , csv



url = "https://www.jumia.com.eg/android-phones/?page="
page = 1
a = True
while a:
  payload={}
  headers = {
        'authority': 'www.jumia.com.eg',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'accept': 'application/json',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'referer': 'https://www.jumia.com.eg/smartphones/',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
      }
  response = requests.request("GET", url+str(page), headers=headers).json()
  x = response.get("viewData")
  y = x.get("products")
  c = 0
  if y == None :
        break
  else:
        def jumia(*args):
              # self.sku = sku
              # self.NAME = NAME
              # self.CATEGORIES = CATEGORIES
              # self.PRICES = PRICES 
              # self.rating = rating
              conn = psycopg2.connect(database="automated_price_comparison", user = "postgres", password = "dana20499", host = "127.0.0.1", port = "5432")
              cur = conn.cursor()
              list = []
              payload={}
              # response = requests.request("GET", url, headers=headers, data=payload)
              for item in y:
                    j=[item['sku'],item['name'],item['categories'],item['prices']['price'],item['rating']["average"]]
                    cur.execute("INSERT INTO JUMIA(SKU,NAME,CATEGORIES,PRICES,RATING) VALUES(%s,%s,%s,%s,%s)",(j))  
                    p = json.loads(payload)
                    print(p[y]["sku"])
                    print(p[y]["NAME"])
                    print(p[y]["CATEGORIES"])
                    print(p['prices']['price'])
                    print(p['rating']["average"])
                    # return(ku,NAME,CATEGORIES,PRICES,rating)
                    conn.commit()
                    conn.close()
              c +=1
  page +=1      

  # z = jumia(p)





# # url = "https://www.jumia.com.eg/redmi-note-7-6.3-inch-64gb-dual-sim-4g-mobile-phone-neptune-blue-xiaomi-mpg166709.html"
# url = "https://www.jumia.com.eg/smartphones/?page="
# page = 1
# a = True
# while a:
#     payload={}
#     headers = {
#     'authority': 'www.jumia.com.eg',
#     'pragma': 'no-cache',
#     'cache-control': 'no-cache',
#     'accept': 'application/json',
#     'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-dest': 'empty',
#     'referer': 'https://www.jumia.com.eg/xiaomi-redmi-note-8-6.3-inch-64gb4gb-mobile-phone-space-black-15421326.html',
#     'accept-language': 'en-US,en;q=0.9,ar;q=0.8',

#     }

#     response = requests.request("GET", url, headers=headers, data=payload).json()
#     x = response.get("viewData")
#     y = x.get("products")

    
#     class jumia(self,sku,NAME,CATEGORIES,PRICES,rating):
#             conn = psycopg2.connect(database="automated_price_comparison", user = "postgres", password = "dana20499", host = "127.0.0.1", port = "5432")
#             cur = conn.cursor()
#             self.sku = sku
#             self.NAME = NAME
#             self.CATEGORIES = CATEGORIES
#             self.PRICES = PRICES 
#             self.rating = rating
#             # print(self.sku ,self.NAME ,self.CATEGORIES ,self.PRICES ,self.rating)  
#             payload={}
#             response = requests.request("GET", url, headers=headers, data=payload).json()
#             p = json.loads(payload)
#             print(p[y]["sku"])
#             print(p["NAME"])
#             print(p["CATEGORIES"])
#             print(p['prices']['price'])
#             print(p['rating']["average"])
#             cur.execute("INSERT INTO JUMIA(SKU,NAME,CATEGORIES,PRICES,RATING) VALUES(%s,%s,%s,%s,%s)")
#             conn.commit()
#             conn.close()
#             return(conn,cur)
#     table()
#     time.sleep(3)
# else:
#     break
#     page +=1

# class price_history:
#     pass
# class caregory:
#     pass