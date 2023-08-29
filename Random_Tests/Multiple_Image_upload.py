from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


driver = webdriver.Firefox()

for i in range(1, 3):
    driver.get("https://codepen.io/mseche/pen/oOVXLg")
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//input[@id='input1']").send_keys(f"/home/tipl-pc-21/Desktop/Images/{i}.png")
    driver.find_element(By.XPATH, "//button[@class='btn btn-big green']").click()
    time.sleep(5)
