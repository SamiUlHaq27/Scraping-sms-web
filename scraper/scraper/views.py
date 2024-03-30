from django.http import HttpResponse
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from time import sleep


def home(request):
    if request.method == "GET":
        opts = Options()
        brw = Chrome(options=opts)
        brw.implicitly_wait(10)
        url = request.GET.get("url")
        brw.get(url)
        # sleep(30)
        html = brw.page_source
        brw.close()
    return HttpResponse(html)
    
