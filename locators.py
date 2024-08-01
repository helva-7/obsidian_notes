import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#Chrome Driver service
driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH,"(//input[@name='name'])[1]").send_keys("mkbouti")
driver.find_element(By.NAME, "email").send_keys("hello@oui.com ")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("mkbouti")
driver.find_element(By.ID, "exampleCheck1").click()
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
driver.find_element(By.ID, "inlineRadio2").click()
driver.find_element(By.NAME,"bday").send_keys("10/14/2002")
# to create an Xpath ,syntax => //tagname[@attribute='value'] , tagname is the type of element , attribut is the
# attribut of the html tag
driver.find_element(By.XPATH,"//input[@type='submit']").click()
driver.find_element(By.XPATH,"(//input[@name='name'])[2]").send_keys("reweave")
driver.find_element(By.XPATH,"(//input[@name='name'])[2]").clear()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)


time.sleep(6)
