import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice")

options = driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")

for option in options:
    if option.get_attribute("value") == "option2":
        option.click()
        assert option.is_selected()
        break

radiobuttons = driver.find_elements(By.CSS_SELECTOR,".radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected(), "iror"




time.sleep(5)