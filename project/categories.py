import requests , json , csv , psycopg2 

url = "https://www.jumia.com.eg/categories/navigation/"

payload={}
headers = {
  'authority': 'www.jumia.com.eg',
  'cache-control': 'max-age=0',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-user': '?1',
  'sec-fetch-dest': 'document',
  'referer': 'https://www.jumia.com.eg/android-phones/',
  'accept-language': 'en-US,en;q=0.9',
  'cookie': '__cfduid=d2546313a05cfdf0dbab9dcb36f44cabe1611534025; newsletter=1; sb-closed=true; userLanguage=en_EG; _gcl_au=1.1.178726863.1611534110; _ga=GA1.3.114356797.1611534110; _gid=GA1.3.1457195316.1611534110; _fbp=fb.2.1611534110973.1653998322; _cs_ex=1521463256; _cs_c=1; sponsoredUserId=3854593961188445027600e5773debe5; SOLSESSID=e455dc8d9f89f0ffa8921a0cb2cb3107; __cf_bm=cbcd2092dcea96c0567b750361361050b56e7eb5-1611555086-1800-ATgUgws08FFpZDm51i1C/H1Tn0Z2v0YwzZLNGkkjUmeUWGM7xPrHtWj1i2s4i645qcTW6mJiHYATg6IdAL5BOU8=; cto_bundle=UX2mSV9HSWpOVW5VYllwZWh4WUdWTnc5aUZKSjdQWHlYOE13aGxuVVMxeFBCYWVqNG1ZRWs4M0hyTmlMcUZ5U1RBNEdDVzByWW5xbTk0ZDBwQU9rclEwV3JSWGxDQUgyS0x5U0syUGFyNGZtZXdtd0J2ckpNWEVmakhaczFyajNJV3ZxcQ; __cfduid=d3d2403de403ef386f442946e8e0f02421609424859; sponsoredUserId=28069313709362049785feddfdb65954; newsletter=1; userLanguage=ar_EG; sb-closed=true; subscriberId=cb18d5e4ff9003775b9d4bc3d7ae80b6; customerType=new; userId=5888064; customerUuid=70673e4e-d068-4fbe-a92d-2f2fb22aedfc; JSC=syv6wM1IuYq-TUD6MpyOuTs4jjtV48czi2z7lRU2gwtrzXTU1VpFfEweFTPlxQzb0yWcUyeXfGjsn6Nbg-n8Lx5MfYRnVz7QA1YoLRb8Ox1USmNAyqafAH_7Cz-LEr_-ZZ8Ju9yUZ7Tpnw9L7b8vxx5pZPYUwontKDWmnPyBz0h2Uux-Lw7z4wfAzaEPEd8jPsCLugEntZjQcQbxPu2Jprszl1xoCdGGQ00gJdYPJEPerbYJWyX2Q1NHjFLwMipvVFPFwOyhSD_uW_d4QQovBOkMydH_JHIZV3Rdq6phfx9ZZau20rYBRlpUlPC36Fw2; accountType=Customer; SOLSESSID=c663c0806bba9fff7d7b2fb9573183be'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
