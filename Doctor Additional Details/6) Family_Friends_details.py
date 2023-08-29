from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
import time
driver = webdriver.Firefox()
driver.maximize_window()
check = driver.current_url

driver.get("http://165.22.217.185")
driver.find_element("name", "LoginId").send_keys("employee")
driver.find_element("name", "Password").send_keys("123123123")
driver.find_element(By.XPATH, "//div[button/@type='submit']").click()

driver.implicitly_wait(5)
driver.get("http://165.22.217.185/layout/doctorDetail/9")
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//*[@id='pr_id_6_header_0']").click()
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//span[@class='btn btn-primary mb-3 float-end']").click()
driver.implicitly_wait(5)
actions = ActionChains(driver)

driver.find_element(By.XPATH, "//input[@name='FamilyAndFriendName']").send_keys("asdasd ")
actions.send_keys(Keys.TAB).send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()
actions.send_keys(Keys.TAB).send_keys("10/11/2012").send_keys(Keys.TAB).send_keys(Keys.TAB).perform()
actions.send_keys("11/12/2013").perform()


driver.find_element(By.XPATH, " //input[@name='FamilyAndFriendSpeicialDay']").send_keys(" 12")
actions.send_keys(Keys.TAB).send_keys("12/12/2014").send_keys(Keys.TAB).perform()
driver.find_element(By.XPATH, " //textarea[@name='Remarks']").send_keys("comments")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(2)
if check == "http://165.22.217.185/layout/doctorDetail/9":
    print("success")
else:
    print("Some error")

