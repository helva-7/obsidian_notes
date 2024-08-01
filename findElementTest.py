import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise")

driver.find_element(By.ID,"autosuggest").send_keys("Mor")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a ")
print(len(countries))
for elem in countries:
    if elem.text == "Morocco":
        elem.click()
        break
assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "Morocco","zbi"
time.sleep(5)