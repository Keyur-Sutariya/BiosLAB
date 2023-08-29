from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import S
from selenium.webdriver.common.alert import Alert

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('http://autopract.com/selenium/alert5/')

driver.find_element(By.ID, 'alert-button').click()
alert = Alert(driver)
print(alert.text)
alert.accept()
driver.find_element(By.ID,'confirm-button').click()
alert.dismiss()