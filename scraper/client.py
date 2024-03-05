import requests

html = requests.get(url="http://127.0.0.1:8000?url=http://127.0.0.1:5500/page1.html")

print(html.text)