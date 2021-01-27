import requests , psycopg2 , csv , json

url = "https://www.jumia.com.eg/smartphones/?page="

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
            def jumia(*args, **kwargs):
                  conn = psycopg2.connect(database="automated_price_comparison", user = "postgres", password = "dana20499", host = "127.0.0.1", port = "5432")
                  cur = conn.cursor()
                  for item in y:
                        j=[item['sku'],item['name'],item['categories'],item['prices']['price'],item['rating']["average"]]
                        cur.execute("INSERT INTO JUMIA(SKU,NAME,CATEGORIES,PRICES,RATING) VALUES(%s,%s,%s,%s,%s)",(j))  
                        response = requests.request("GET",  url, headers=headers, data=payload)
                        payload={}
                        p = json.loads(payload)
                        print(p[y]["sku"])
                        print(p[y]["name"])
                        print(p[y]["categories"])
                        print(p['prices']['price'])
                        print(p['rating']["average"])
                        conn.commit()
                        conn.close()
                  c +=1
            def price_history(kwa):
                  conn = psycopg2.connect(database="automated_price_comparison", user = "postgres", password = "dana20499", host = "127.0.0.1", port = "5432")
                  cur = conn.cursor()
                  for item in y:    
                        b=[item['prices']['price']]
                        cur.execute("INSERT INTO PRICE_HISTORY (PRICES) values (%s)",(b))  
                        response = requests.request("GET",  url, headers=headers, data=payload)
                        payload={}
                        p = json.loads(payload)
                        print(p['prices']['price'])
                        conn.commit()
                        conn.close()
                  c +=1
      page +=1      
          # jumia()
          # price_history()

'''

class database:
    def __init__(self, parma):
        self.conn = psycopg2.connect(parma)
        self.cur = self.conn.cursor()

    def query(self, query):
        self.cur.execute(query)
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()
db = database(**params)
db.query(""" CREATE TABLE parts (part_id SERIAL PRIMARY KEY,part_name VARCHAR(255) NOT NULL)""")

'''