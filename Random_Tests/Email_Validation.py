from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import re

driver= webdriver.Firefox()
print("Enter an Email")

email = driver.find_element(By.XPATH, " //input[@id='username']")

if re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$)", email):
    print("Valid")

else:
    print("Invalid")
