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
driver.get("http://165.22.217.185/layout/doctorDetail/9")
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//*[@id='pr_id_16_header_0']").click()
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//span[@class='btn btn-primary mb-3 float-end']").click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, " //input[@name='ProceduralEquipmentName']").send_keys("Xyz")
driver.find_element(By.XPATH, "//input[@name='ProceduralEquipmentVendorName']").send_keys("Xyz")
actions.send_keys(Keys.TAB).send_keys("21/12/2023").perform()
driver.find_element(By.XPATH, "//input[@name='ProceduralEquipmentPrice'] ").send_keys("52000")
driver.find_element(By.XPATH, " //textarea[@name='Remarks']").send_keys("Remarks")
driver.find_element(By.XPATH, " //button[@type='submit']").click()