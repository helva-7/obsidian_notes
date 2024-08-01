import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#Chrome Driver service
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")

driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")
password="123456"
driver.find_element(By.XPATH,"//form/div[2]/input").send_keys(password)
driver.find_element(By.XPATH,"//form/div[3]/input").send_keys(password)
driver.find_element(By.XPATH,"//form/div[4]/button").click()
time.sleep(5)
