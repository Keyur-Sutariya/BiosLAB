from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import selenium.webdriver.common
from selenium.webdriver.firefox.service import service
import time

driver = webdriver.Firefox()
driver.get("http://165.22.217.185")
driver.find_element("name", "LoginId").send_keys("employee")
driver.find_element("name", "Password").send_keys("123123123")
driver.find_element(By.XPATH, "//div[button/@type='submit']").click()

time.sleep(5)

driver.get("http://165.22.217.185/layout/submaster/chemistContactPerson")
time.sleep(4)

driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
time.sleep(3)

(driver.find_element(By.XPATH, "//div[@class=' css-1wy0on6']")).click()
(driver.find_element(By.XPATH, "//div[@class=' css-1wy0on6']")).get_attribute("")
values = driver.find_element(By.CSS_SELECTOR, "div. css-1dimb5e-singleValue").get_attribute("")

print(values)
time.sleep(4)
