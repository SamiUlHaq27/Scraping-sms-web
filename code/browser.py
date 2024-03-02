from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class Browser:
    
    def __init__(self) -> None:
        opt = Options()
        self.brw = webdriver.Chrome(options=opt)

    def get(self, url):
        try:
            self.brw.implicitly_wait(10)
            self.brw.get(url)
            time.sleep(5)
            content = self.brw.page_source
        except Exception as e:
            print(e)
        return content
        
    def close(self):
        self.brw.close()
