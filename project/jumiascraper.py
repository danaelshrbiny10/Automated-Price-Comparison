import requests , psycopg2 , csv

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
      c = 0                                                                                  ## counter for loop
      if y == None :
        break
      else:
            for item in y:
                    # a = y[c]["name"]                                                                               ## get name of each product
                    conn = psycopg2.connect(database="automated_price_comparison", user = "postgres", password = "dana20499", host = "127.0.0.1", port = "5432")
                    cur = conn.cursor()                                                                               ## to connect with DB
                    # print(y[c]["prices"])                                                                           ##  get price of each product
                    V = [y[c]["name"],y[c]['url']]                                                                    ## get name  & url of each product
                    # z = y[c]['url']
                    D="insert into category (NAME , url) values (%s ,%s)"                                             ## put data into category
                    b = [(V[0]) , (V[1])]                                                                             ## obtains name & url in 2 col
                    cur.execute(D, b)
                    # print(a)
                    conn.commit()
                    # print ("Records created successfully");
                    conn.close()
            c +=1
      page +=1
      
    