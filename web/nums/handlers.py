from .modules import countries_crawler, numbers_crawler, sms_crawler, crawler
import datetime
import json
from TPN.settings import BASE_DIR
from .models import Country, Number, Message
from .sides import slugify


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
        print(time_elapsed)
        if(time_elapsed < 720):
            print("time not come")
            return 1
        
        html = crawler.get(country.link)
        if html == "empty":
            print("empty response")
            return 0
        
        total_pages = crawler.getLastPageNo(html)
        numbers = numbers_crawler.fetchNumbers(html)
        
        # for i in range(2, total_pages+1):
        #     try:
        #         html = numbers_crawler.getPageNo(country.link, country.name, i, refresh=refresh)
        #         if html =="empty":
        #             break
        #         numbers += numbers_crawler.fetchNumbers(html)
        #     except Exception as e:
        #         print(e)
        
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
        total_pages = crawler.getLastPageNo(html)
        
        data = sms_crawler.fetchData(html)
        number.active_since = data["since"]
        number.status = data["status"]
        number.save()
        
        messages = sms_crawler.fetchSms(html)
        
        # for i in range(2, total_pages+1):
        #     try:
        #         html = sms_crawler.getPageNo(number.link, number.number, i, refresh=refresh)
        #         if html == "empty":
        #             break
        #         messages += sms_crawler.fetchSms(html)
        #     except Exception as e:
        #         print(e)
        
        for message in messages:
            if Messages.doesExist(message["text"]):
                pass
            else:
                msg = Message()
                msg.at_time = message["time"]
                msg.from_sndr = message["from"]
                msg.text = message["text"]
                msg.number = number.number
                msg.save()
                number.sms += 1
                number.save()
        
    def doesExist(text:str):
        objs = Message.objects.filter(text=text)
        if len(objs) > 0:
            return True
        else:
            return False