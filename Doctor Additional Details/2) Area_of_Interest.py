from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://165.22.217.185")

driver.find_element("name", "LoginId").send_keys("employee")
driver.find_element("name", "Password").send_keys("123123123")
driver.find_element(By.XPATH, "//div[button/@type='submit']").click()
time.sleep(1)

driver.get("http://165.22.217.185/layout/doctorDetail/1")
time.sleep(1)

driver.find_element(By.XPATH, "//a[@id='pr_id_2_header_0']").click()

time.sleep(1)
driver.find_element(By.XPATH, " //span[normalize-space()='Add Area Of Interest']").click()
time.sleep(1)
action = ActionChains(driver)
action.send_keys(Keys.TAB).send_keys(Keys.TAB).perform()
action.send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()

driver.find_element(By.XPATH, " //textarea[@name='Remarks']").send_keys("Remarks")



