import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys

driver = webdriver.Firefox()
action = ActionChains(driver)

list1 = random.randrange(20,30)
#random_value = random.choice(list1)


def drop():
    action.send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()


driver.get("https://formstone.it/components/dropdown/demo/")

driver.find_element(By.XPATH, " //button[@id='demo_label-dropdown-selected']").send_keys(Keys.ENTER)

for k in range(list1):
    drop()

print("Randomly selected number is : ", list1)
action.click()
