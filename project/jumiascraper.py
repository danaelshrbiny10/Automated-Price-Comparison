import requests

url = "https://www.jumia.com.eg/smartphones/?page=2"

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
response = requests.request("GET", url, headers=headers).json()
print(response)

# print(response.text)


x = response.get("viewData")
y = x.get("products")
c = 0
for item in y:
      print(y[c]["name"])
      print(y[c]["prices"])
      
      
      c +=1