import time
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By


Browser = webdriver.Firefox()
Browser.get("http://165.22.217.185")
Browser.find_element("name", "LoginId").send_keys("employee")
Browser.find_element("name", "Password").send_keys("123123123")
Browser.find_element(By.XPATH, "//div[button/@type='submit']").click()

time.sleep(5)
Browser.get("http://165.22.217.185/layout/submaster/chemistContactPerson")
time.sleep(4)
Browser.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
time.sleep(3)

Browser.find_element(By.XPATH, "//div[@class=' css-1wy0on6']").click()
time.sleep(2)

Browser.find_element(By.XPATH,"//input[@name='ChemistContactPersonName']").send_keys('Random')
Browser.find_element(By.XPATH,"//input[@name='Email']").send_keys("random@random.com")
Browser.find_element(By.XPATH,"//input[@name='MobileNo']").send_keys("1221")
Browser.find_element(By.XPATH,"//input[@name='ChemistContactPersonAddressLine1']").send_keys("Ahmedabad")
Browser.find_element(By.XPATH,"//input[@name='ChemistContactPersonAddressLine2']").send_keys("Gandhinagar")
Browser.find_element(By.XPATH,"//div[@class=' css-1wy0on6']").click()
time.sleep(2)
#Browser.find_element(By.XPATH,"//div[contains(@class,'css-t3ipsp-control')]//div[contains(@class,'css-19bb58m')]").click()

time.sleep(5)
Browser.find_element(By.XPATH,"//button[@type='submit']").click()

while True:
  pass