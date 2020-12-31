# -*- coding: utf-8 -*-
import requests , urllib
from bs4 import BeautifulSoup
from requests import *
url = 'https://www.jumia.com.eg/ar/smartphones/?page=2'


headers = {
  'authority': 'www.jumia.com.eg',
  'pragma': 'no-cache',
  'cache-control': 'no-cache',
  'accept': 'application/json',
  'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.jumia.com.eg/ar/smartphones/?page=2',
  'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
  'cookie': '__cfduid=d18c424466b4a03640eeea0b162b221ed1605877389; newsletter=1; sb-closed=true; _gcl_au=1.1.1814548577.1605877391; _ga=GA1.3.1313839063.1605877392; _fbp=fb.2.1605877392227.964332060; _cs_ex=1521463256; _cs_c=1; sponsoredUserId=37252672192985794515fb7be935e30d; userLanguage=ar_EG; __gads=ID=d67cac8530f7555a:T=1606322258:S=ALNI_MZNz6r5jkWjL4tk4cs1rG6ar67p5g; closedBanners=1726%2C1745%2C1744%2C1752%2C1762%2C1764%2C1765%2C1778; _gid=GA1.3.1621353031.1606682274; SOLSESSID=91b4930bee68e9b9cf56f466eb63dcf1; _gcl_aw=GCL.1606688039.Cj0KCQiAqo3-BRDoARIsAE5vnaLPCNfKO8pHM611H4ETnbDHRvirYJ8lj70JSZo5lSXRGtdjT-YTBHQaAl60EALw_wcB; _gac_UA-33473298-1=1.1606688061.Cj0KCQiAqo3-BRDoARIsAE5vnaLPCNfKO8pHM611H4ETnbDHRvirYJ8lj70JSZo5lSXRGtdjT-YTBHQaAl60EALw_wcB; _fbc=fb.2.1606688245832.IwAR2G_wC2Wgt7RsJrxfPn4hFcY2c6yLUc4cOkmGHAL8DvFnJwpVAUH5Bicdk; cto_bundle=XGePf19uWk1jc01lRnVqMERnN0tkY25DNmdFT0FYNGVSTGtuWEVaUHJ3MjNneXdyJTJCMWp6TFFiU0g4Wkx2TTdoYmk2dUFjMFBGMFhnSEt4ZiUyQiUyRm9aWVlpcHlOJTJGWVV5RFFwaGhzOE5neUc1UkhwVlB6ekFwczJobnZ0JTJCS21ZczFOJTJGVFBLUzVpZ3BlQVMwbFY0cyUyRjY4YktKYTBIdyUzRCUzRA; _gat_UA-33473298-1=1; sb-closed=true; SOLSESSID=91b4930bee68e9b9cf56f466eb63dcf1'
}


response = requests.request("GET", url, headers=headers).json()
print(response)