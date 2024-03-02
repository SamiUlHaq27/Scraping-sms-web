from django.db import models
from .modules import countries_crawler, numbers_crawler, sms_crawler

refresh = False

class Country(models.Model):
    
    name = models.CharField(max_length=50)
    link = models.URLField()
    numbers = models.IntegerField(default=0)
    slug_id = models.CharField(max_length = 50, default="oops")
    
    def __str__(self):
        return self.name

class Number(models.Model):
    
    number = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    active_since = models.CharField(max_length=20)
    sms = models.IntegerField(default=0)
    link = models.URLField()
    slug_id = models.CharField(max_length = 50, default="oops")
    
    def __str__(self) -> str:
        return self.number

class Message(models.Model):
    
    number = models.CharField(max_length=50)
    at_time = models.CharField(max_length=20)
    from_sndr = models.CharField(max_length=20)
    text = models.TextField()
    
    def __str__(self) -> str:
        return f"[{self.from_sndr} : {self.at_time}]"

class Countries:

    def update():
        html = countries_crawler.get(refresh=refresh)
        if html == "empty":
            return 0
        total_pages = countries_crawler.getTotalPages(html)
        countries = countries_crawler.fetch_countries(html)
        
        for i in range(2,total_pages+1):
            try:
                html = countries_crawler.getPageNo(i)
                if(html=="empty"):
                    break
                countries += countries_crawler.fetch_countries(html)
            except Exception as e:
                print(e)
            
        for country in countries:
            if(Countries.doesExist(country["name"])):
                pass
            else:
                obj = Country()
                obj.name = country["name"]
                obj.link = country["link"]
                obj.slug_id = slugify(country["name"])
                obj.save()
            
    def doesExist(name):
        objs = Country.objects.filter(name=name)
        if len(objs) > 0:
            return True
        else:
            return False

class Numbers:
    
    def update(country:Country):
        html = numbers_crawler.get(country.name, country.link, refresh=refresh)
        if html == "empty":
            return 0
        total_pages = numbers_crawler.getLastPage(html)
        numbers = numbers_crawler.fetchNumbers(html)
        
        for i in range(2, total_pages+1):
            try:
                html = numbers_crawler.getPageNo(country.link, country.name, i, refresh=refresh)
                if html =="empty":
                    break
                numbers += numbers_crawler.fetchNumbers(html)
            except Exception as e:
                print(e)
        
        for number in numbers:
            if(Numbers.doesExist(number["number"])):
                pass
            else:
                obj = Number()
                obj.number = number["number"]
                obj.link = number["link"]
                obj.country = country.name
                obj.slug_id = slugify(number["number"])
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
        html = sms_crawler.get(number.number, number.link, refresh=refresh)
        if html == "empty":
            return 0
        total_pages = sms_crawler.getLastPageNo(html)
        
        data = sms_crawler.fetchData(html)
        number.active_since = data["since"]
        number.status = data["status"]
        number.save()
        
        messages = sms_crawler.fetchSms(html)
        
        for i in range(2, total_pages+1):
            try:
                html = sms_crawler.getPageNo(number.link, number.number, i, refresh=refresh)
                if html == "empty":
                    break
                messages += sms_crawler.fetchSms(html)
            except Exception as e:
                print(e)
        
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

def slugify(string):
    res = ""
    for c in string:
        if c  == ' ':
            res += '-'
        elif c.isalnum():
            res += c
        else:
            pass
    return res



