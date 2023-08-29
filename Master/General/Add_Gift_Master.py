from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
import time

options = Options()
driver = webdriver.Chrome()
options.add_argument("user-data-dir=/tmp/TIPL-PC-21")

driver.get("http://165.22.217.185")
driver.find_element("name", "LoginId").send_keys("employee")
driver.find_element("name", "Password").send_keys("123123123")
driver.find_element(By.XPATH, "//div[button/@type='submit']").click()

time.sleep(5)

driver.get("http://165.22.217.185/layout/master/general/AddGiftMaster")

time.sleep(5)

driver.find_element(By.NAME, "GiftCode").send_keys("123")
driver.find_element(By.NAME, "GiftName").send_keys("SmartPhone")
driver.find_element(By.NAME, "GiftSmscode").send_keys("321")
driver.find_element(By.NAME, "GiftPrice").send_keys("5000")
driver.find_element(By.NAME, "Remark").send_keys("Superb")
time.sleep(2)
driver.find_element(By.NAME, "ChemistGift").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "css-13cymwt-control").click()

time.sleep(5)

driver.get("http://165.22.217.185/layout/master/general/AddHoliday")
driver.find_element(By.ID, "holiday").click()
time.sleep(5)
driver.find_element(By.ID, "react-select-2-input").click()
#customLoc =
driver.find_element(By.XPATH, "//option[text()='" + "Banglore" + "']").click()

while True:
    pass
