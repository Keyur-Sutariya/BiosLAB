import time

from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

js = 'alert("Successfully Logged in")'

dashboard = 'http://165.22.217.185/layout/dashboard'
driver.get(" http://165.22.217.185/")
driver.find_element(By.XPATH, "//input[@placeholder='Please enter username'] ").send_keys("MrManager")
driver.find_element(By.XPATH, "//input[@placeholder='Please enter password'] ").send_keys("123123123")
driver.find_element(By.XPATH, "//button[@type='submit'] ").click()

time.sleep(2)
current = driver.current_url
if current == dashboard:
    print("Successfully Logged in ")
    driver.execute_script(js)
    time.sleep(2)
else:
    print("Some error")
    driver.execute_script('alert("Some Error")')
    time.sleep(1)
driver.quit()
