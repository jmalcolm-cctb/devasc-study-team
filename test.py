import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service('/usr/bin/chromedriver'))

url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url)

elements = driver.find_elements(By.CSS_SELECTOR, "#articlecount a")
print(elements[0].text)

driver.close()

