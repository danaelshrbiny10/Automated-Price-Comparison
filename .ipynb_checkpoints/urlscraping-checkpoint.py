from bs4 import BeautifulSoup
import requests


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
