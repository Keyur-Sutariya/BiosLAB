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

driver.find_element(By.XPATH, "//*[@id='pr_id_17_header_0']").click()
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//span[@class='btn btn-primary mb-3 float-end']").click()
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//input[@name='BankName']").send_keys("HDFC")
driver.find_element(By.XPATH, "//input[@name='AccountNo']").send_keys("9512369741")
driver.find_element(By.XPATH, "//input[@name='IFsccode']").send_keys("9512369741")
driver.find_element(By.XPATH, "//input[@name='AccountHolderName']").send_keys("MRM")
check = driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)
if check:
    print("Error")
else:
    print("No Error")
