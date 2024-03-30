from .modules import countries_crawler, numbers_crawler, sms_crawler, crawler
import datetime
import json
from TPN.settings import BASE_DIR
from .models import Country, Number, Message
from .sides import slugify
from .time_mng import getTime


class Countries:

    def update():
        html = crawler.get("https://temporary-phone-number.com/countrys/")
        if html == "empty":
            return 0
        
        total_pages = crawler.getLastPageNo(html)
        countries = countries_crawler.fetch_countries(html)
        
        for i in range(2,total_pages+1):
            try:
                html = countries_crawler.getPageNo(i)
                countries += countries_crawler.fetch_countries(html)
            except Exception as e:
                print(e)
        
        with open(BASE_DIR/"Flags.json", 'r') as f:
            data = json.load(f)
        
        for country in countries:
            if(Countries.doesExist(country["name"])):
                pass
            else:
                obj = Country()
                obj.name = country["name"]
                obj.link = country["link"]
                obj.slug_id = slugify(country["name"])+"-Phone-Number"
                obj.flag = data[obj.name]
                obj.save()
            
    def doesExist(name):
        objs = Country.objects.filter(name=name)
        if len(objs) > 0:
            return True
        else:
            return False

class Numbers:
    
    def update(country:Country):
        
        dif = datetime.datetime.now() - country.updated_at.replace(tzinfo=None)
        time_elapsed = dif.seconds
        print("Last refresh seconds ago = ",time_elapsed)
        if(time_elapsed < 7200):
            print("time not come")
            return 1
        
        html = crawler.get(country.link)
        if html == "empty":
            print("empty response")
            return 0
        
        numbers = numbers_crawler.fetchNumbers(html)
        Numbers.insert(numbers, country)
        
        # total_pages = crawler.getLastPageNo(html)
        # print("Total pages: ",total_pages)
        # for i in range(2, total_pages+1):
        #     try:
        #         html = numbers_crawler.getPageNo(country.link, i)
        #         if html =="empty":
        #             break
        #         numbers = numbers_crawler.fetchNumbers(html)
        #         Numbers.insert(numbers, country)
        #     except Exception as e:
        #         print(e)
        
    def insert(numbers:Number, country:Country):
        for number in numbers:
            if(Numbers.doesExist(number["number"])):
                pass
            else:
                obj = Number()
                obj.number = number["number"]
                obj.link = number["link"]
                obj.country = country.name
                obj.slug_id = slugify(number["number"])
                obj.country_flag = country.flag
                obj.country_slug = country.slug_id
                obj.save()
                country.numbers += 1
        country.save()
    
    def doesExist(number):
        objs = Number.objects.filter(number=number)
        if len(objs) > 0:
            return True
        else:
            return False

class Messages:
    
    def update(number:Number):
        
        dif = datetime.datetime.now() - number.updated_at.replace(tzinfo=None)
        print(dif.seconds)
        if(dif.seconds < 30):
            return 1
        
        html = crawler.get(number.link)
        if html == "empty":
            return 0
        
        data = sms_crawler.fetchData(html)
        number.active_since = data["since"]
        number.status = data["status"]
        number.save()
        
        messages = sms_crawler.fetchSms(html)
        Messages.insert(messages, number)
        
        # total_pages = crawler.getLastPageNo(html)
        # print("Total pages: ",total_pages)
        # for i in range(2, total_pages+1):
        #     try:
        #         html = sms_crawler.getPageNo(number.link, number.number, i, refresh=refresh)
        #         if html == "empty":
        #             break
        #         messages += sms_crawler.fetchSms(html)
        #     except Exception as e:
        #         print(e)
        
    def insert(messages, number:Number):
        i = len(messages)
        while(i>=0):
            i -= 1
            message = messages[i]
            if Messages.doesExist(message["text"]):
                pass
            else:
                # print(getTime(message["time"]))
                msg = Message()
                msg.from_sndr = message["from"]
                msg.text = message["text"]
                msg.number = number.number
                msg.at_time = getTime(message["time"])
                msg.save()
                number.sms += 1
        number.save()
        
    def doesExist(text:str):
        objs = Message.objects.filter(text=text)
        if len(objs) > 0:
            return True
        else:
            return False