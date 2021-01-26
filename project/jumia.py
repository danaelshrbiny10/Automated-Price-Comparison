import requests, psycopg2 , json , time , csv



url = "https://www.jumia.com.eg/android-phones/?page="

# page = 1

payload={}
headers = {
  'authority': 'www.jumia.com.eg',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 OPR/73.0.3856.284',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-dest': 'document',
  'referer': 'https://www.jumia.com.eg/phones-tablets/',
  'accept-language': 'en-US,en;q=0.9',
  'cookie': '__cfduid=d2546313a05cfdf0dbab9dcb36f44cabe1611534025; newsletter=1; sb-closed=true; userLanguage=en_EG; _gcl_au=1.1.178726863.1611534110; _ga=GA1.3.114356797.1611534110; _gid=GA1.3.1457195316.1611534110; _fbp=fb.2.1611534110973.1653998322; _cs_ex=1521463256; _cs_c=1; SOLSESSID=01f4b40d76e78ab1be4243463572c3c0; __cf_bm=c31f0090828ae5dae1e480469aa6c788ebe32d19-1611552446-1800-Ac1Ma+GRAi5tkQP878mTiZrQQx8OcitkxSu4NCJJ6AxdUyi+35d2um7yRWqcas/OpdqVuPSsd0t6gIsBOK97tzQ=; sponsoredUserId=3854593961188445027600e5773debe5; __cfduid=d3d2403de403ef386f442946e8e0f02421609424859; sponsoredUserId=28069313709362049785feddfdb65954; newsletter=1; userLanguage=ar_EG; sb-closed=true; subscriberId=cb18d5e4ff9003775b9d4bc3d7ae80b6; customerType=new; userId=5888064; customerUuid=70673e4e-d068-4fbe-a92d-2f2fb22aedfc; JSC=syv6wM1IuYq-TUD6MpyOuTs4jjtV48czi2z7lRU2gwtrzXTU1VpFfEweFTPlxQzb0yWcUyeXfGjsn6Nbg-n8Lx5MfYRnVz7QA1YoLRb8Ox1USmNAyqafAH_7Cz-LEr_-ZZ8Ju9yUZ7Tpnw9L7b8vxx5pZPYUwontKDWmnPyBz0h2Uux-Lw7z4wfAzaEPEd8jPsCLugEntZjQcQbxPu2Jprszl1xoCdGGQ00gJdYPJEPerbYJWyX2Q1NHjFLwMipvVFPFwOyhSD_uW_d4QQovBOkMydH_JHIZV3Rdq6phfx9ZZau20rYBRlpUlPC36Fw2; accountType=Customer; __cf_bm=573eee5f718bf924aabf35862d09059d596301c3-1611552779-1800-AUDvj2g1ZZvbOiZJSo/xQJq8Pa10H3lnUyaUJLY4FeqAjUfzgXocAG2kn5S0sGriMyu6dwwkiwgfCCG18ZAYz10=; SOLSESSID=ff362d12ffd2d60742d0876281b27fef'
  }
response = requests.request("GET", url, headers=headers, data=payload).json()
x = response.get("viewData")
y = x.get("products")
c = 0
def jumia(self,sku,NAME,CATEGORIES,PRICES,rating):
      self.sku = sku
      self.NAME = NAME
      self.CATEGORIES = CATEGORIES
      self.PRICES = PRICES 
      self.rating = rating
      conn = psycopg2.connect(database="automated_price_comparison", user = "postgres", password = "dana20499", host = "127.0.0.1", port = "5432")
      cur = conn.cursor()
      list = []
      payload={}
      response = requests.request("GET", url, headers=headers, data=payload)
      x = response.get("viewData")
      y = x.get("products")
      for item in y:    
          p = json.loads(payload)
          print(p[y]["sku"])
          print(p[y]["NAME"])
          print(p[y]["CATEGORIES"])
          print(p['prices']['price'])
          print(p['rating']["average"])
          return(ku,NAME,CATEGORIES,PRICES,rating)
          cur.execute("INSERT INTO JUMIA(SKU,NAME,CATEGORIES,PRICES,RATING) VALUES(%s,%s,%s,%s,%s)")
          conn.commit()
          conn.close()
      c +=1

z = jumia()








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