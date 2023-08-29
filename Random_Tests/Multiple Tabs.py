import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import urllib.request
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
actions = ActionChains(driver)
driver.maximize_window()

driver.get('https://www.google.co.in')

images = driver.find_element(By.XPATH, "//a[@aria-label='Search for Images (opens a new tab)']")
driver.execute_script("window.open('images')")
time.sleep(3)
#actions.key_down(Keys.CONTROL).click(images).key_up(Keys.CONTROL).perform()
print(driver.current_url)
