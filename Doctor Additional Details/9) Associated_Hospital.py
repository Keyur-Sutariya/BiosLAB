from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
import time

driver = webdriver.Firefox()
driver.maximize_window()
actions = ActionChains(driver)

check = driver.current_url

driver.get("http://165.22.217.185")
driver.find_element("name", "LoginId").send_keys("employee")
driver.find_element("name", "Password").send_keys("123123123")
driver.find_element(By.XPATH, "//div[button/@type='submit']").click()

driver.implicitly_wait(5)
driver.get("http://165.22.217.185/layout/doctorDetail/9")
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//*[@id='pr_id_9_header_0']").click()
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//span[@class='btn btn-primary mb-3 float-end']").click()
driver.find_element(By.XPATH, "//input[@name='AssociatedHospitalName']").send_keys("SMS")
actions.send_keys(Keys.TAB).send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()
driver.find_element(By.XPATH, " //input[@name='AssociatedHospitalActive']").click()
actions.send_keys(Keys.TAB).send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()
driver.find_element(By.XPATH, "//input[@name='AssociatedHospitalMonthly']").send_keys("SMS")
driver.find_element(By.XPATH, "//input[@name='AssociatedHospitalWeekly']").send_keys("SMS")
driver.find_element(By.XPATH, "//input[@name='AssociatedHospitalDaily']").send_keys("SMS")
actions.send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@name='AssociatedHospitalAddressLine1']").send_keys("SMS")
driver.find_element(By.XPATH, "//input[@name='AssociatedHospitalAddressLine2']").send_keys("SMS")
actions.send_keys(Keys.TAB).send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()
time.sleep(2)
actions.send_keys(Keys.TAB).send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()
driver.find_element(By.XPATH, " //button[@type='submit']").click()


