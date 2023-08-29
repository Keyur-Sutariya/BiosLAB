from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Firefox()

driver.maximize_window()

driver.get("http://demo.automationtesting.in/FileUpload.html")
driver.get_credentials("Username", " Password")

driver.find_element(By.XPATH, "//*[@id='input-4']").send_keys("/home/tipl-pc-21/Desktop/favicon.png")










