import requests , psycopg2 , csv , json

url = "https://www.jumia.com.eg/smartphones/?page="
# page = ["url"]
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
      # print(response)
      # print(response.text)

      ## obtains products from json 
      x = response.get("viewData")
      y = x.get("products")
      c = 0
      if y == None :
        break
      else:
            for item in y:
                    conn = psycopg2.connect(database="automated_price_comparison", user = "postgres", password = "dana20499", host = "127.0.0.1", port = "5432")
                    cur = conn.cursor()                                                                               ## to connect with DB
                    V = [y[c]["name"],y[c]['url']]                                                                    ## get name  & url of each product
                    category = "INSERT INTO category (NAME , url) values (%s ,%s)"                                    ## put data into category
                    b = [(V[0]) , (V[1])]                                                                             ## obtains name & url in 2 col with index from V
                    cur.execute(category, b)                                                                          ## execute category & index
                    #----------------------------------------------------------------------------------------------------------------------
                    j = [y[c]['sku'],y[c]['name'],y[c]['categories'],y[c]['prices']['price'],y[c]['rating']['totalRatings']]
                    jumiaa = "INSERT INTO JUMIA (SKU,NAME,CATEGORIES,PRICES,rating) values (%s ,%s , %s , %s, %s)"
                    n = [(j[0]) , (j[1]), (j[2]), (j[3]), (j[4])]
                    cur.execute(jumiaa, n)
                    #-----------------------------------------------------------------------------------------------------------------------
                    p = [y[c]['prices']['price']]
                    price = "INSERT INTO PRICE_HISTORY (PRICES) values (%s)"
                    q = [(p[0])]
                    cur.execute(price, q)
                    conn.commit()
                    conn.close()
            c +=1
      page +=1
      
