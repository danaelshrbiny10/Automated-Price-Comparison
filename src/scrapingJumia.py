import requests
import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from jumia.models import Jumia
from products.models import category

Categories = [
    # {"id": 1, "url": "playstation-5-consoles", "verbose": "Games Console"},
    # {"id": 2, "url": "playstation-5-accessories", "verbose": "Games Console Accessories"},
    # {"id": 4, "url": "virtual-reality-phones-tablets", "verbose": "VR"},
    # {"id": 5, "url": "mobile-phones", "verbose": "Mobile Phone"},
    # {"id": 6, "url": "tablets", "verbose": "Tablet"},
    # {"id": 7, "url": "laptops", "verbose": "Laptop Notebook"},
    # {"id": 10, "url": "computer-networking-switches", "verbose": "Network Switch"},
    # {"id": 11, "url": "computer-networking-routers", "verbose": "Routers"},
    # {"id": 12, "url": "computer-keyboards", "verbose": "Keyboards"},
    # {"id": 13, "url": "computer-components-computer-cases", "verbose": "Computer Casing"},
    {"id": 15, "url": "mobile-phone-accessories-cables", "verbose": "Cables"},
    {"id": 16, "url": "laptop-chargers-adapters", "verbose": "Laptop Charger"},
    {"id": 17, "url": "mobile-phone-bluetooth-headsets", "verbose": "Headphones and Headsets"}, 
    {"id": 18, "url": "mobile-phone-memory-cards", "verbose": "Memory Card"},
    {"id": 19, "url": "mobile-accessories", "verbose": "Mobile Phone Accessories"}, 
    {"id": 20, "url": "mobile-phone-accessories-power-banks", "verbose": "Power Banks"},
    {"id": 22, "url": "tablet-accessories", "verbose": "Tablet Accessories"},  
    {"id": 23, "url": "smart-watches", "verbose": "Smart Watches"},     
]

headers = {
  'authority': 'www.jumia.com.eg',
  'pragma': 'no-cache',
  'cache-control': 'no-cache',
  'accept': 'application/json',
  'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.jumia.com.eg/laptops/',
  'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
}
def getFullCategory(url="playstation-5-consoles",page=1):
    categUrl = f"https://www.jumia.com.eg/{url}/?page={page}"       
    response = requests.request("GET", categUrl, headers=headers).json()
    tri=response['viewData']
    if not 'pagination' in response['viewData']:
        return(None)
    else:
        x=response['viewData']['products']
        return(x)


# url = "https://www.jumia.com.eg/mobile-phones/?page=1"

# response = requests.request("GET", url, headers=headers).json()
# x=response['viewData']['products']

# for items in x :
    # sku=items["sku"]
    # title=items["name"]
    # image_url=items["image"]
    # primary_link=items["url"]
    # lastprice=items["prices"]['rawPrice']
    # manufacturer=items["brand"]
    # # fullDescription=getDescription(primary_link)
    # fullDescription="getDescription(primary_link)"
    # active=True
    # rating=items['rating']["average"]

def dbSave(URL,id):
    i=0
    pages=1
    while getFullCategory(URL,page=pages):
        fulldata=getFullCategory(URL,page=pages)
        for items in fulldata:
            sku=items["sku"]
            title=items["name"]
            try:
                image_url=items["image"]
            except:
                image_url=None

            primary_link=items["url"]
            lastprice=items["prices"]['rawPrice']
            manufacturer=items["brand"]
            fullDescription="em Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentia"
            active=True
            rating=items['rating']["average"]
            categoryObj=category.objects.get(pk=id)
            try:
                c=Jumia.objects.create(sku=sku,title=title,manufacture=manufacturer,description=fullDescription,img=image_url,url=primary_link,active=True,lastprice=lastprice,rate=rating,category=categoryObj)
                c.save()
            except:
                pass
            print(i)
            i=i+1
        pages=pages+1
        print(pages)

for c in Categories:
    print(f"scraping{c['verbose']} now ")
    dbSave(c['url'],c['id'])
