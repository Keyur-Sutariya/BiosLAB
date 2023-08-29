import time

from  selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.wikipedia.org")
time.sleep(3)
action = ActionChains(driver)
action.send_keys(Keys.F5).perform()
time.sleep(3)
query = driver.find_element("id", "searchInput")
query.send_keys("Hello World")
query.submit()


print(driver.find_element("id", "firstHeading").text)
while True:
    pass



