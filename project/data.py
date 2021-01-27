import requests , psycopg2 , csv , json

def connn():
    conn = psycopg2.connect(database="automated_price_comparison", user = "postgres", password = "dana20499", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    return(conn , cur) 

    
def jumia(j):
    conn,cur = connn() 
    c=0
    print(j)
    for item in y:
        m=[item['sku'],item['name'],item['categories'],item['prices']['price'],item['rating']["average"]]
        cur.execute("INSERT INTO JUMIA(SKU,NAME,CATEGORIES,PRICES,RATING) VALUES(%s,%s,%s,%s,%s)",(m)) 
        conn.commit()
        c +=1
    conn.close()
        


url = "https://www.jumia.com.eg/smartphones/?page="

page = 1
a = True
while a:
    payload={}
    headers = { 'authority': 'www.jumia.com.eg', 'pragma': 'no-cache', 'cache-control': 'no-cache', 'accept': 'application/json', 'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1', 'referer': 'https://www.jumia.com.eg/smartphones/',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',}
    response = requests.request("GET", url+str(page), headers=headers).json()
    x = response.get("viewData")
    y = x.get("products")
    if y == None :
        break
jumia(y)