import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Chrome Driver service
driver = webdriver.Chrome()
# service_object = Service("\Users\\24000006\\Downloads\\chromedriver-win64.zip\\chromedriver-win64.exe")
# driver.Chrome(service=service_obk)
driver.get("https://google.com")  #use this approach , its better
driver.maximize_window()
title = driver.title
print(title)
current_url=driver.current_url
print(current_url)
time.sleep(5)
