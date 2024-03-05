from . import crawler
from bs4 import BeautifulSoup


def fetchData(html):
    soup = BeautifulSoup(html, "html.parser")
    
    data = {}
    target = soup.find('table',"table-striped").find_all('tr')
    data["status"] = target[0].find_all('td')[1].text
    data["since"] = target[-1].find_all('td')[1].text
    
    return data

def fetchSms(html):
    soup = BeautifulSoup(html, "html.parser")
    
    target = soup.find('div','direct-chat-messages')
    target = target.find_all('div','left')
    
    messages = []
    for sms in target:
        try:
            item = {}
            info = sms.find('div','direct-chat-info')
            item["time"] = info.find('time').text
            item["from"] = info.find('span','pull-right').text.replace("From ","")
            item["text"] = sms.find('div','direct-chat-text').text
            messages.append(item)
        except Exception as e:
            # print(e)
            pass
    
    return messages

def getPageNo(main_url, page_no):
    html = crawler.get(url = main_url+"/page"+str(page_no))
    return html