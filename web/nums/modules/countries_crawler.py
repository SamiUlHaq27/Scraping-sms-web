from . import crawler
from bs4 import BeautifulSoup



def get(url="https://temporary-phone-number.com/countrys/" ,page="", refresh=False):

    if(refresh):
        html = crawler.get(url)
        crawler.write("cpage"+page, html)
    else:
        html = crawler.load("cpage"+page)

    return html

def fetch_countries(html) -> list:
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div","col-sm-6 col-md-4 col-lg-3 col-xs-12")
    countries = []
    for item in items:
        link = item.a.attrs["href"]
        name = item.find('span','info-box-number').text
        countries.append({
            "name":name,
            "link":link
        })
    
    return countries

def getTotalPages(html):
    no = crawler.getLastPageNo(html)
    return int(no)

def getPageNo(no, refresh=False):
    if no==1:
        no = ""
    else:
        no = str(no)
    html = get(url="https://temporary-phone-number.com/countrys/"+"page"+no, page=no, refresh=refresh)
    return html