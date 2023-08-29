import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

options = Options()
driver = webdriver.Chrome(options)


options.add_argument("user-data-dir=/tmp/TIPL-PC-21")

driver.get("http://165.22.217.185")
driver.find_element("name", "LoginId").send_keys("employee")
driver.find_element("name", "Password").send_keys("123123123")
driver.find_element(By.XPATH, "//div[button/@type='submit']").click()

time.sleep(5)
# some other code in the same tab
driver.get("http://165.22.217.185/layout/master/general/AddCFA")
time.sleep(5)
driver.find_element("name", "Name").send_keys("KKK")
driver.find_element("name", "Code").send_keys("123")
driver.find_element("name", "Place").send_keys("Ahmedabad")
driver.find_element("name", "ContactPerson").send_keys("asdfs")
driver.find_element("name", "Address1").send_keys("qwe")
driver.find_element("name", "Address2").send_keys("rty")
driver.find_element("name", "Address3").send_keys("iop")

driver.find_element("name", "MobileNo").send_keys("7897897891")
driver.find_element("name", "Phone").send_keys("9879879877")
driver.find_element("name", "Email").send_keys("abc@123.com")
driver.find_element("name", "DLno1").send_keys("9879879877")
driver.find_element("name", "DLno2").send_keys("9879879877")
driver.find_element("name", "Gst").send_keys("9879879877")
driver.find_element("name", "Fssai").send_keys("9879879877")
driver.find_element("name", "NRX").send_keys("9879879877")
driver.find_element("name", "Other").send_keys("9879879877")
time.sleep(5)
x = driver.find_element(By.CLASS_NAME, " css-13cymwt-control").click()
drop = Select(x)
time.sleep(5)
drop.select_by_visible_text("Gujarat")
driver.find_element(By.XPATH, "//div[button/@type='submit']").click()

while True:
    pass
