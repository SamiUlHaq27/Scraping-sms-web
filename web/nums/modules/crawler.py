from bs4 import BeautifulSoup
import requests


def get(url):
    try:
        response = requests.get("http://127.0.0.1:9000/?url="+url)
        return response.text
    except Exception as e:
        print(e)
        return "empty"

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
    return int(link.split("page")[-1])

