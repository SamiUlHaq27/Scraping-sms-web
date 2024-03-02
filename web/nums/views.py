from django.shortcuts import render
from .models import Countries, Numbers, Country, Number, Messages, Message
import random
from django.core import paginator

def index(request):
    content = {}
    #-------------------------------------------------------
    content["four_countries"] = random.sample(list(Country.objects.all()), 4)
    content["four_numbers"] = random.sample(list(Number.objects.all()), 4)
    #-------------------------------------------------------
    response = render(request, 'nums/index.html', content)
    return response

def countries(request):
    content = {}
    #-------------------------------------------------------
    content["countries"] = Country.objects.all()
    #-------------------------------------------------------
    response = render(request, 'nums/countries.html', content)
    return response

def numbers(request, country):
    content = {}
    #-------------------------------------------------------
    content["country"] = Country.objects.filter(slug_id=country)[0]
    #-------------------------------------------------------
    content["three_countries"] = random.sample(list(Country.objects.all()), 3)
    # content["numbers"] = []
    # for country in content["three_countries"]:
    #     content["numbers"].append(random.sample(list(Number.objects.filter(country=country.name)), 4))
    #-------------------------------------------------------
    try:
        content["pageNo"] = int(request.GET.get('page-no'))
    except:
        content["pageNo"] = 1
    pagination = paginator.Paginator(Number.objects.filter(country=content["country"].name), 10)
    content["numbers"] = pagination.get_page(content["pageNo"])
    content["last_page_no"] = pagination.num_pages
    content["pages"] = get_pages(content["numbers"], content["pageNo"], content["last_page_no"])
    #-------------------------------------------------------
    response = render(request, 'nums/numbers.html', content)
    return response

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
    pagination = paginator.Paginator(Message.objects.filter(number=number.number), 20)
    content["messages"] = pagination.get_page(content["pageNo"])
    content["last_page_no"] = pagination.num_pages
    content["pages"] = get_pages(content["messages"], content["pageNo"], content["last_page_no"])
    #-------------------------------------------------------
    response = render(request, 'nums/messages.html', content)
    return response

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

            
    # if page.has_previous():
    #     pages.insert(0, page.previous_page_number())
    # else:
    #     next_page_no = page.next_page_number()
    #     if next_page_no+2 <= last_page:
    #         pages.append(next_page_no+2)
            
    return pages