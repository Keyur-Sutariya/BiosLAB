from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://165.22.217.185")

driver.find_element("name", "LoginId").send_keys("employee")
driver.find_element("name", "Password").send_keys("123123123")
driver.find_element(By.XPATH, "//div[button/@type='submit']").click()
time.sleep(3)

driver.get("http://165.22.217.185/layout/doctorDetail/1")
time.sleep(1)

driver.find_element(By.XPATH, "//a[@id='pr_id_5_header_0']").click()

time.sleep(3)

driver.find_element(By.XPATH, "//span[@class='btn btn-primary mb-3 float-end']").click()

time.sleep(2)

action = ActionChains(driver)
action.send_keys(Keys.TAB).send_keys(Keys.TAB).perform()
action.send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()
action.send_keys(Keys.TAB).send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()
driver.find_element(By.XPATH, "//input[@name='WeekendAndVacationActivityPlace']").send_keys("Ahmedabad")
action.send_keys(Keys.TAB).send_keys("07/08/2023").perform()
driver.find_element(By.XPATH, "//textarea[@name='Remarks']").send_keys("Remarks")
time.sleep(3)
