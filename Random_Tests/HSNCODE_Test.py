import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

i=2
j=2
driver = webdriver.Firefox()

driver.get("http://165.22.217.185")
driver.find_element("name", "LoginId").send_keys("employee")
driver.find_element("name", "Password").send_keys("123123123")
driver.find_element(By.XPATH, "//div[button/@type='submit']").click()
time.sleep(3)


driver.get("http://165.22.217.185/layout/AddProduct")
driver.find_element(By.XPATH, "//input[@name='Name']").send_keys("abc")
action = ActionChains(driver)
action.send_keys(Keys.TAB).send_keys("Bottles").send_keys(Keys.ENTER).perform()
driver.find_element(By.XPATH, "//input[@name='HsnCode']").send_keys(j, "541", i)