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
            def connn():
                  conn = psycopg2.connect(database="automated_price_comparison", user = "postgres", password = "dana20499", host = "127.0.0.1", port = "5432")
                  cur = conn.cursor()
                  return(conn , cur) 

            def jumia(j):
                  conn,cur = connn() 
                  c=0
                  print(j)
                  for item in y:
                        J = [item['sku'],item['name'],item['categories'],item['prices']['price'],item['rating']["average"]]
                        cur.execute("INSERT INTO JUMIA(SKU,NAME,CATEGORIES,PRICES,RATING) VALUES(%s,%s,%s,%s,%s)",(J)) 
                        conn.commit()
                        c +=1
                  conn.close()
            jumia(y)   

            def price_history(b):
                  conn , cur = connn()
                  c = 0
                  print(b)
                  for item in y:
                        B = [item['prices']['price']]
                        cur.execute("INSERT INTO PRICE_HISTORY (PRICES) values (%s)",(B)) 
                        conn.commit()
                        c +=1
                  conn.close()
            price_history(y)

            def category(v):
                  conn , cur = connn()
                  c = 0
                  print(v)
                  for item in y:  
                        V = [item["name"],item['url']]    
                        cur.execute("INSERT INTO category (NAME , url) values (%s ,%s)",(V))
                        conn.commit()
                        c +=1
                  conn.close()
            category(y)        
      page +=1      

def main_category(f):
            conn , cur = connn()
            c = 0
            print(f)
            list = [['laptops'],['mobile-phones'],['mobile-accessories'],['electronic-television-video'],['cameras'],['home-audio-electronics'],['electronics-headphone'],['computer-data-storage'],['computing-accessories'],['computer-components'],['computer-accessories'],['networking'],['pc-gaming'],['laystation-games'],['digital-games'],['xbox-games']]
            for items in list:
                  print(items)
                  cur.execute("INSERT INTO MAIN_CATEGORY (categories) values (%s)",(items))
                  conn.commit()
            conn.close()
main_category(y)