from .models import Number, Country
import json
from django.core import paginator


def get_pages(page:paginator.Paginator, current_page, last_page):
    pages = [current_page]
    
    if page.has_next():
        pages.append(page.next_page_number())
        if current_page+2 <= last_page:
            pages.append(current_page+2)


    if page.has_previous():
        pages.insert(0, page.previous_page_number())
        if current_page-2 > 0:
            pages.insert(0, current_page-2)
            
    return pages

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

#------------------------------- Once Used ----------------------------

def setFlag():
    objs = Number.objects.all()
    
    for obj in objs:
        country = obj.country
        flag = Country.objects.filter(name=country)[0].flag
        obj.country_flag = flag
        obj.save()

def getFlags():
    
    objs = Country.objects.all()
    data = {}
    for obj in objs:
        data[obj.name] = obj.flag
    with open("Flags.json",'w') as f:
        json.dump(data, f, indent=2)

def sulgifyCountriesNumbers():
    
    objs = Number.objects.all()
    for obj in objs:
        country = obj.country
        obj.country_slug = Country.objects.filter(name=country)[0].slug_id
        obj.save()
  
def sulgifyCountries():
    
    objs = Country.objects.all()
    for obj in objs:
        obj.slug_id += "-Phone-Number"
        obj.save()
