import countries_crawler
import numbers_crawler
import sms_crawler


html = countries_crawler.get(refresh=False)
countries = countries_crawler.fetch_countries(html)
total_pages = countries_crawler.getTotalPages(html)
ct = countries[0]

html = numbers_crawler.get(ct["name"], ct["link"], refresh=False)
total_pages = numbers_crawler.getLastPage(html)
numbers = numbers_crawler.fetchNumbers(html)
nb = numbers[0]

html = sms_crawler.get(nb["number"], nb["link"], refresh=False)
total_pages = sms_crawler.getLastPageNo(html)
messages = sms_crawler.fetchSms(html)

countries_crawler.getPageNo(2, refresh=False)
numbers_crawler.getPageNo(ct["link"], ct["name"], page_no=3, refresh=False)
sms_crawler.getPageNo(nb["link"], nb["number"], 5, refresh=True)