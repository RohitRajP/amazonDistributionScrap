import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# constructing URL to get to the items listing page
url = "https://www.amazondistribution.in/search?size=2page=1&ref_=sr_nr_crf_department"

# creating a browser instace of google chrome
browser = webdriver.Chrome(ChromeDriverManager().install())

# opening the URL in the webDriver
browser.get(url)
browser.get(url)

while True:
    
    print("Scolling")

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)") 

    if browser.find_elements_by_css_selector('#ws-nav-footer'):
        break

    time.sleep(2)



