from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Firefox()
driver.maximize_window()
actions = ActionChains(driver)

driver.get("http://165.22.217.185")

driver.find_element("name", "LoginId").send_keys("employee")
driver.find_element("name", "Password").send_keys("123123123")
driver.find_element(By.XPATH, "//div[button/@type='submit']").click()

driver.implicitly_wait(5)

driver.get("http://165.22.217.185/layout/master/general/Holiday")
driver.find_element(By.XPATH, "//button[@class='btn btn-outline-primary mt-2 mx-2'] ").click()
actions.send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys("21/12/2023").perform()
driver.find_element(By.XPATH, "//input[@id='holiday'] ").click()
driver.find_element(By.XPATH, "//input[@name='HolidayName']").send_keys("Public Holiday")
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div/div[4]/div/div/div[1]/div[2]/div").click()
actions.send_keys("Gujarat").send_keys(Keys.ENTER).perform()
driver.find_element(By.XPATH, " //input[@name='Reason']").send_keys("Reason")
driver.find_element(By.XPATH, "//button[@type='submit']").click()