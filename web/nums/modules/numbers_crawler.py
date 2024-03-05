from . import crawler
from bs4 import BeautifulSoup

        
def fetchNumbers(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div","col-sm-6 col-md-4 col-lg-3 col-xs-12")
    numbers = []
    for item in items:
        try:
            num = {}
            link = item.find("a").attrs["href"]
            num["link"] = link
            num["country"] = item.find("span", "info-box-text").text
            num["number"] = item.find("span", "info-box-number").text
            numbers.append(num)
        except Exception as e:
            pass
    return numbers
    
def getPageNo(main_url, page_no):
    html = crawler.get(url = main_url+"page"+str(page_no))
    return html