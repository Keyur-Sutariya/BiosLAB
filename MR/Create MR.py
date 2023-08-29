from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.maximize_window()
actions = ActionChains(driver)

driver.get("http://165.22.217.185/")
driver.find_element(By.XPATH, " //input[@placeholder='Please enter username']").send_keys("employee")
driver.find_element(By.XPATH, " //input[@placeholder='Please enter password']").send_keys("123123123")
driver.find_element(By.XPATH, " //button[@type='submit']").click()

driver.implicitly_wait(10)
driver.get("http://165.22.217.185/layout/AddMR")
time.sleep(5)

