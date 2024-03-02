import crawler
from bs4 import BeautifulSoup

def get(number, url, page="", refresh=False):
    if refresh:
        html = crawler.get(url)
        crawler.write(number+page, html)
    else:
        html = crawler.load(number+page)
    return html

def getLastPageNo(html):
    no = crawler.getLastPageNo(html)
    return int(no)

def fetchSms(html):
    soup = BeautifulSoup(html, "html.parser")
    
    data = {}
    target = soup.find('table',"table-striped").find_all('tr')
    data["status"] = target[0].find_all('td')[1].text
    data["since"] = target[-1].find_all('td')[1].text
    
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
            print(e)
    
    return messages

def getPageNo(main_url, number, page_no, refresh=False):
    html = get(
        number = number,
        url = main_url+"/page"+str(page_no),
        page = "_"+str(page_no),
        refresh = refresh
        )
    return html