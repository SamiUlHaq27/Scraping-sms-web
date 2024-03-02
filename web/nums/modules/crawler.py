from .browser import Browser
from bs4 import BeautifulSoup

    
path = __file__.replace("crawler.py","")

def get(url):
    try:
        brw = Browser()
        html = brw.get(url)
        brw.close()
    except Exception as e:
        print(e)
        html = "empty"
    return html

def write(filename, html):
    with open(path+f"pages/{filename}.html", 'w', encoding="utf-8") as f:
        f.write(html)
        
def load(filename):
    try:
        with open(path+f"pages/{filename}.html",'r') as f:
            html = f.read()
    except Exception as e:
        print(e)
        html = "empty"
    return html

def getLastPageNo(html):
    soup = BeautifulSoup(html, "html.parser")
    try:
        pagination = soup.find("ul","pagination")
        aas = pagination.find_all("a")
    except Exception as e:
        print(e)
        return 0
    for a in aas:
        number = a.text
        try:
            link = a.attrs["href"]
            if number=="End":
                break
        except:
            pass
    return link.split("page")[-1]

