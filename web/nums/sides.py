from django.core import paginator
import datetime


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

