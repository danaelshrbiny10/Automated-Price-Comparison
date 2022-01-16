
from datetime import timezone
from celery import Celery, shared_task
from accounts.models import Profile
from project.celery import app
from products.models import notifyme, priceHistory
from souq.models import Souq
from notifications.signals import notify
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.mail import send_mail

import requests

payload={}
headers = {
'authority': 'egypt.souq.com',
'pragma': 'no-cache',
'cache-control': 'no-cache',
'accept': 'application/json, text/javascript, */*; q=0.01',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
'x-requested-with': 'XMLHttpRequest',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': 'https://egypt.souq.com/eg-ar/keyboard/l/',
'Cookie': 'COCODE_EG=eg; PHPSESSID=ec0ebf08466d4eb75954d3115fc0421b; PLATEFORMC=eg; PLATEFORML=en; c_Ident=16063459803197; BUYER_CITY_SELECTED=27'
}
import re

payload={}
headers = {
'authority': 'egypt.souq.com',
'pragma': 'no-cache',
'cache-control': 'no-cache',
'accept': 'application/json, text/javascript, */*; q=0.01',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
'x-requested-with': 'XMLHttpRequest',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': 'https://egypt.souq.com/eg-ar/keyboard/l/',
'Cookie': 'COCODE_EG=eg; PHPSESSID=ec0ebf08466d4eb75954d3115fc0421b; PLATEFORMC=eg; PLATEFORML=en; c_Ident=16063459803197; BUYER_CITY_SELECTED=27'
}
@shared_task
def priceChanged():
    url = "https://egypt.souq.com/eg-en/search_results.php?action=quickView&id="
    c=Souq.objects.all()
    
    for item in c:
        try:
            found = re.search('(?<=-)(\d+)(?=/i/)', item.url).group(1)
            response = requests.request("GET", url+found, headers=headers, data=payload).json()
            soquD=Souq.objects.get(pk=item.id)
            try:
                print(float(response["price"]["current_price"].strip(' EGP').replace(',','')) )
                c=priceHistory.objects.create(souq=soquD,timeDate=timezone.now(),lastprice=float(response["price"]["current_price"].strip(' EGP').replace(',','')))
                c.save()
                soquD.lastprice=float(response["price"]["current_price"].strip(' EGP').replace(',',''))
                soquD.save()
            except:
                soquD.active=False
                soquD.save()
        except AttributeError:
            print(None) #TO do do your handling
@shared_task
def notificationsTasks():
    c=notifyme.objects.all()
    for i in c:
        soquD=Souq.objects.get(pk=i.souqid)
        b=priceHistory.objects.all().filter(souq=soquD)
        for item in b:
            if item.lastprice>soquD.lastprice:
                profile = Profile.objects.get(user =User.objects.get(username=i.username) )
                sender = User.objects.get(username=profile)
                receiver = User.objects.get(username=profile)
                Souq.objects.get(pk=i.souqid).title
                notify.send(sender, recipient=receiver, verb='Message', description=f"the product with title { Souq.objects.get(pk=i.souqid).title} has changed and the current price is { Souq.objects.get(pk=i.souqid).lastprice}")    
                send_mail("price change ", f"the product with title { Souq.objects.get(pk=i.souqid).title} has changed and the current price is { Souq.objects.get(pk=i.souqid).lastprice}", "dj88co@gmail.com", [User.objects.get(username=i.username).email], fail_silently = False)
                print('done2')
        else:
                print("none")
    return 'done'
