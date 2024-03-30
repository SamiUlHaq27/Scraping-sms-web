from .models import Number, Country
import json


def deleteZero():
    objs = Country.objects.filter(numbers="0")
    for obj in objs:
        obj.delete()


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
