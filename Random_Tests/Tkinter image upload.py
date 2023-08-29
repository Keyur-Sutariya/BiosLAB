import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.firefox import service

driver = webdriver.Firefox()


driver2 = webdriver.Firefox(service=service)

driver.implicitly_wait(15)
driver.get('https://www.iloveimg.com/resize-image')

upload_file = driver.find_element(By.XPATH,'//*[@id="pickfiles"]')
# upload_file.send_keys(r"C:\cover.png")
# trying to import the file using the file browser function, as send_keys function didn't work
upload_file.click()
time.sleep(3)
pyautogui.typewrite(r'/home/tipl-pc-21/Desktop/favicon.png')
pyautogui.press('enter')