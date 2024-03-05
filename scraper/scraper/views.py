from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def home(request):
    if request.method == "GET":
        url = request.GET.get("url")
        print(url)
    try:
        opt = Options()
        brw = webdriver.Chrome(options=opt)
        brw.implicitly_wait(10)
        brw.get(url)
        html = brw.page_source
    except Exception as e:
        print(e)
        html = "empty"
    return HttpResponse(html)