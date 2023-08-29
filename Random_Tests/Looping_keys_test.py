import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
i=1
driver = webdriver.Firefox()
driver.get("https://www.shutterstock.com/images")

action = ActionChains(driver)
Button_Down = action.send_keys(Keys.DOWN)

while i < 10:
    Button_Down.perform()
    time.sleep(2)
    i = i+1

driver.quit()
