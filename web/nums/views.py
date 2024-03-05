from django.shortcuts import render
from .models import Country, Number, Message
from .handlers import Countries, Numbers, Messages
import random
from django.core import paginator
from .sides import get_pages
import json




def index(request):
    content = {}
    #-------------------------------------------------------
    content["four_countries"] = random.sample(list(Country.objects.all()), 4)
    content["four_numbers"] = random.sample(list(Number.objects.all()), 4)
    #-------------------------------------------------------
    response = render(request, 'nums/index.html', content)
    return response

def countries(request):
    # Countries.update()
    content = {}
    #-------------------------------------------------------
    content["countries"] = Country.objects.all()
    #-------------------------------------------------------
    response = render(request, 'nums/countries.html', content)
    return response

def numbers(request, country):
    content = {}
    #-------------------------------------------------------
    print(country)
    content["country"] = Country.objects.get(slug_id=country)
    print(content["country"])
    Numbers.update(content["country"])
    #-------------------------------------------------------
    content["usa_cnt"] = Country.objects.filter(name="United States")[0]
    content["usa_num"] = Number.objects.filter(country="United States")[:3]
    content["uk_cnt"] = Country.objects.filter(name="United Kingdom")[0]
    content["uk_num"] = Number.objects.filter(country="United Kingdom")[:3]
    content["frn_cnt"] = Country.objects.filter(name="France")[0]
    content["frn_num"] = Number.objects.filter(country="France")[:3]
    #-------------------------------------------------------
    try:
        content["pageNo"] = int(request.GET.get('page-no'))
    except:
        content["pageNo"] = 1
    numbers = list(Number.objects.filter(country=content["country"].name))
    pagination = paginator.Paginator(numbers, 10)
    content["numbers"] = pagination.get_page(content["pageNo"])
    content["last_page_no"] = pagination.num_pages
    content["pages"] = get_pages(content["numbers"], content["pageNo"], content["last_page_no"])
    #-------------------------------------------------------
    return render(request, 'nums/numbers.html', content)

def messages(request, country, number):
    content = {}
    #-------------------------------------------------------
    number = Number.objects.filter(slug_id=number)[0]
    content["number"] = number
    Messages.update(number)
    #-------------------------------------------------------
    content["three_countries"] = random.sample(list(Country.objects.all()), 3)
    #-------------------------------------------------------
    try:
        content["pageNo"] = int(request.GET.get('page-no'))
    except:
        content["pageNo"] = 1
    messages = list(Message.objects.filter(number=number.number))
    pagination = paginator.Paginator(messages, 20)
    content["messages"] = pagination.get_page(content["pageNo"])
    content["last_page_no"] = pagination.num_pages
    content["pages"] = get_pages(content["messages"], content["pageNo"], content["last_page_no"])
    #-------------------------------------------------------
    content["usa_cnt"] = Country.objects.filter(name="United States")[0]
    content["usa_num"] = Number.objects.filter(country="United States")[:3]
    content["uk_cnt"] = Country.objects.filter(name="United Kingdom")[0]
    content["uk_num"] = Number.objects.filter(country="United Kingdom")[:3]
    content["frn_cnt"] = Country.objects.filter(name="France")[0]
    content["frn_num"] = Number.objects.filter(country="France")[:3]
    #-------------------------------------------------------
    response = render(request, 'nums/messages.html', content)
    return response

def about(request):
    return render(request, "about.html")