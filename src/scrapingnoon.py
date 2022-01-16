import requests
import os
import django
import sys
import time
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from noon.models import Noon
from products.models import category

Categories = [
    {"id": 1, "url": ['electronics-and-mobiles/video-games-10181'], "verbose": "Games Console"},
    {"id": 4, "url": "virtual-reality-phones-tablets", "verbose": "VR"},
    {"id": 5, "url": ['electronics-and-mobiles/mobiles-and-accessories'], "verbose": "Mobile Phone"},
    {"id": 8, "url": ['electronics-and-mobiles/computers-and-accessories'], "verbose": "Computers"},
    {"id": 23, "url": ['electronics-and-mobiles/wearable-technology'], "verbose": "Smart Watches"},     
]
headers = {
'authority': 'www.noon.com',
'pragma': 'no-cache',
'cache-control': 'no-cache, max-age=0, must-revalidate, no-store',
'x-locale': 'en-eg',
'x-content': 'mobile',
'x-mp': 'noon',
'x-platform': 'web',
'x-cms': 'v2',
'content-type': 'application/json',
'accept': 'application/json, text/plain, */*',
'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
'origin': 'https://www.noon.com',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': 'https://www.noon.com/egypt-en/electronics-and-mobiles/mobiles-and-accessories/mobiles-20905/apple',
'accept-language': 'en-US,en;q=0.9,ar;q=0.8',}

def getFullCategory(url=['electronics-and-mobiles/wearable-technology'],page=1):
    categUrl = "https://www.noon.com/_svc/catalog/api/search"  
    payload={"brand":[],"category":url,"filterKey":[],"f":{},"sort":{"by":"popularity","dir":"desc"},"limit":50,"page":page}
    try:
        response = requests.request("POST", categUrl, headers=headers, json=payload)
        print(response.status_code)

    except:
        pass
    if(response.status_code==429):
        time.sleep(10)
        v=getFullCategory()
    else:
        response=response.json()
        v=response.get('hits')
    return(v)

# print(getFullCategory())

def dbSave(URL,id):
    i=0
    pages=1
    while getFullCategory(URL,page=pages):
        fulldata=getFullCategory(URL,page=pages)
        for item in fulldata:
            try:
                sku=item['sku']
                title=item["name"]
                offercode=item["offer_code"]
                image_url=item["image_key"]
                primary_link=item["url"]
                if item['sale_price']== None:
                    lastprice=item['price']
                else:
                    lastprice=item['sale_price']
                manufacturer=item["brand"]
                fullDescription="em Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentia"
                if 'product_rating' in item:
                    rating=item['product_rating']['value']
                else:
                    rating=0
                categoryObj=category.objects.get(pk=id)
                # try:
                c=Noon.objects.create(sku=sku,title=title,manufacture=manufacturer,description=fullDescription,img=image_url,url=primary_link,active=True,lastprice=lastprice,rate=rating,category=categoryObj,offercode=offercode)
                c.save()
                print("done")

            except:
                pass

            print(i)
            i=i+1
        pages=pages+1
        print(pages)

for c in Categories:
    print(f"scraping{c['verbose']} now ")
    dbSave(c['url'],c['id'])