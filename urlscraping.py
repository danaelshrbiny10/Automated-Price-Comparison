from bs4 import BeautifulSoup
from requests import *


## creating empty list 
urls = []


## creating function
def scrape(site):
    r = requests.get(site)     ## getting the request from url
    ## converting the text
    s = BeautifulSoup(r.text , "html.parser")  
    for i in s.find_all("a"):
        href = i.attrs["href"]
        if href.startswitch("/"):
            site = site + href
            if site not in urls:
                urls.append(site)
                print(site)
                scrape(site)

## main function
if __name__ == "__main__" :
    site = "https://www.jumia.com.eg/android-phones/"
    scrape(site)               



'''

url = 'https://www.jumia.com.eg/android-phones/'
response =  requests.get(url)
response.status_code

soup = BeautifulSoup(response.content)

## find elements by class 

results = soup.find_all('div' , class_="-pvs col12")
print(results)

all_urls = [results.find('div' , class_="-pvs col12").text.strip for result in results]
        
'''