import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Firefox()
actions = ActionChains(driver)
driver.get("http://165.22.217.185")
driver.find_element("name", "LoginId").send_keys("employee")
driver.find_element("name", "Password").send_keys("123123123")
driver.find_element(By.XPATH, "//div[button/@type='submit']").click()

time.sleep(1)

driver.get("http://165.22.217.185/layout/AddMR")
driver.find_element(By.XPATH, "//input[@name='ExpenseBankAcno']").send_keys("123")
actions.send_keys(Keys.TAB).send_keys("21/11/1994").perform()


time.sleep(1)



