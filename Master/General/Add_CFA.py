import time
from selenium import webdriver
from selenium.webdriver import Firefox

from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://165.22.217.185")
driver.find_element("name", "LoginId").send_keys("employee")
driver.find_element("name", "Password").send_keys("123123123")
driver.find_element(By.XPATH, "//div[button/@type='submit']").click()
time.sleep(5)
driver.get("http://165.22.217.185/layout/AddDoctor")
time.sleep(5)

driver.find_element(By.XPATH, " //input[@name='DoctorName']").send_keys("Doctor")
driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(1) > div:nth-child(17) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2)").click()
while True:
    pass







driver.get("http://165.22.217.185/layout/master/general/AddCFA")
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
driver.find_element("name", "fssai").send_keys("9879879877")
driver.find_element("name", "NRX").send_keys("9879879877")
driver.find_element("name", "Other").send_keys("9879879877")
driver.find_element(By.CLASS_NAME, "DateOfBirth").click()

webDriver.findElement(By.xpath("//span[text()='Next']")).click()
webDriver.findElement(By.xpath("(//a[text()='14'])[3]")).click()

driver.find_element(By.XPATH, "//div[button/@type='submit']")

while True:
    pass




#meh
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div[aria-label='All reviews']"))).click()
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//div[@role='menuitem']//div[text()='"+ selectItem +"']"))).click()

driver.find_element(By.XPATH, "//div[input/@name='DateOfBirth']").click()
